"""Download PDF resources from AWR"""

import requests
import os
import argparse


def parser():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=False)
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help="Show all help messages.")
    parser.add_argument('--min_id', type=int, default=0, required=True,
                        help="Define the start ID for the search range.")
    parser.add_argument('--max_id', type=int, default=23000, required=True,
                        help="Define the end ID for the search range.")
    parser.add_argument('--save_path', type=str, default='AWR', required=True,
                        help="The path to save the downloaded PDF files.")
    args = parser.parse_args()
    return args


def retrieve(min_id=0, max_id=23000, save_path='AWR'):
    # DO NOT CHANGE THE PREFIX USED TO BUILD URLS
    prefix = 'https://www.womenaustralia.info/wp-admin/admin-ajax.php?action=efront_entry_pdf_export&id='
    # use to skip blank PDF files
    skip_mask = r"b'\t<style>\n\t\t*,\n\t\t*::before,\n\t\t*::after"
    
    # create save_path if it does not exist
    if not os.path.exists(save_path):
        os.makedirs(save_path, exist_ok=True)
    
    # update min_id and max_id to download new resources
    for id in range(min_id, max_id):
        url = prefix + str(id)
        response = requests.get(url)
        if response.status_code == 200:
            pdf_name = 'awr_' + str(id) + '.pdf'
            # skip blank files
            if str(response.content).startswith(skip_mask):
                print(f"Skipped blank {pdf_name}")
                continue
            # save as PDF files
            with open(save_path + '/' + pdf_name, "wb") as f:
                f.write(response.content)
                print(f"Saved as {pdf_name}")
        else:
            print(f"Failed to download {pdf_name}." \
                f"Status code: {response.status_code}.")


if __name__ == '__main__':
    args = parser()
    retrieve(args.min_id, args.max_id, args.save_path)
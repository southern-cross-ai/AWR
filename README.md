# The Australian Women's Register (AWR)

## Overview

**Keywords**: Australia; Women; Archive

The [AWR](https://www.womenaustralia.info) is a product of the Australian Women’s Archives Program (AWAP) established in 1999, has long-standing collaboration between the University of Melbourne and the National Foundation for Australian Women (NFAW). 

AWR is created to build knowledge and recognition of the social, cultural, historical and economic contribution made by Australian women to public and private life.

## Data Source

The original data is from [AWR Database](https://www.womenaustralia.info/entries/) and licensed under [CC BY-NC-ND 3.0 AU](https://creativecommons.org/licenses/by-nc-nd/3.0/au/).

Noticed that the original database is constantly updating. The dataset collected in this repo was last updated on **17 Aug 2024**.

The dataset under `AWR_clean` is a cleaned version of the original dataset created by [Xinyu Mao](https://github.com/Xinyu990511). You can download it from [Hugging Face - SouthernCrossAI/AWR_Australian_Womens_Register](https://huggingface.co/datasets/SouthernCrossAI/AWR_Australian_Womens_Register).

## Data Structure

This repo uses `id`s to build URLs to retrieve the `.pdf` resources. You may came across documents from the following aspects:
- Archived Resources
- Award
- Cultural Artefact
- Event
- Exhibition
- Organisation
- Person
- Place
- Published Resources


Under `AWR` directory, there are **20556** `awr_[id].pdf` files collected from [AWR Database](https://www.womenaustralia.info/entries/), where `id` serves as the identifier for each document.


## License

The repo is licensed under [MIT](https://opensource.org/license/mit).
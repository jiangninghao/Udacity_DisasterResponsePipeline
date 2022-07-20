# Udacity_DisasterResponsePipeline
This repository contains all working files for the DisasterResponsePipeline Udacity project

This is for the 2nd project in Udacity Data Scientist nanodegree. Below is the table of contents for this file: 
1. Motivation of the project
2. Python library used
3. Data source
4. File description
5. Instruction for code execution

## Motivation of the project 

1. Run a ETL pipeline that cleans and merge 2 datasets and stores the data in a database 
2. Run a ML pipeline that trains differnt classifiers 

## Python Library used
- numpy
- pandas
- nltk
- sqlalchemy
- sklearn

## Data Source
- 2 csv data files provided by Udacity containing messages and categories information

## File description 
1. messages - inlcude ID, disaster message, original disaster message and genre info
2. categories - later used to create unique categories for each disaster message
3. data_process.py - help run ELT pipeline in Udacity IDE that cleans data and stores in the database
4. train_classifier.py - run ML pipeline that trains calssifier and saves model output

### Instructions for code execution:
1. Run the following commands in the project's root directory to set up your database and model.
    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`
2. Go to `app` directory: `cd app`
3. Run your web app: `python run.py`
4. Click the `PREVIEW` button to open the homepage


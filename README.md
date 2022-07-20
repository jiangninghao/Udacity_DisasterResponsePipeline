# Udacity_DisasterResponsePipeline
This repository contains all working files for the DisasterResponsePipeline Udacity project

This is for the 2nd project in Udacity Data Scientist nanodegree. Below is the table of contents for this file: 
1. Motivation of the project
2. Python library used
3. Data source
4. File description
5. Summary

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
2 csv data files were provided by the Udacity team - messages.csv and categories.csv; 
2 python scripts were also uploaded 

## File description 
messages - inlcude ID, disaster message, original disaster message and genre info
categories - later used to create unique categories for each disaster message
data_process.py - help run ELT pipeline in Udacity IDE that cleans data and stores in the database
train_classifier.py - run ML pipeline that trains calssifier and saves model output

## Summary 
1. ETL result is stored in a SQL database
2. RandomForecastClassifier outperformed DecisionTreeClassifier

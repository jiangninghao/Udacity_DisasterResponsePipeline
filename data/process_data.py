import sys

import pandas as pd
import numpy as np 
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    '''
    Load_data
    Load data from csv files and merge the data into a single dataframe
    
    Input: 
    message_filepath    file path for messages csv file 
    categories_filepath file path for categories csv file 
    
    categories  new data frame of separating 'categories' column into 36 columns by semi-colon
    
    Return:
    df  final data frame merging messages and categories data
    '''
    
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    
    #merge datasets
    df = messages.merge(categories, on='id')
    
    #build a new dataframe by splitting the 'categories' column into 36 columns separated by semi-colon
    categories = df['categories'].str.split(";", expand=True)
    
    #add column names for each splited column 
    row = categories.iloc[0]
    category_colnames = row.apply(lambda x:x[:-2])
    categories.columns = category_colnames
  
    #convert category values to just numbers 0 or 1 
    for column in categories:
        categories[column] = categories[column].str[-1]
        categories[column] = categories[column].astype(int)
        
    #drop the original categories from df
    df = df.drop(['categories'], axis=1)
    
    #drop column 'related' from dataframe because the category contains a multiclass
    categories = categories.drop['related', axis=1)
    
    #concatenate orignal dataframe with the new dataframe 
    df = pd.concat([df, categories], axis=1, join='inner')
    
    return df 


def clean_data(df):
                        
    #drop duplicates from the dataframe
    df = df.drop_duplicates(keep=False)
    

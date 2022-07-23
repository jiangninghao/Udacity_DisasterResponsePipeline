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
    categories = categories.drop(['related'], axis=1)
    
    #concatenate orignal dataframe with the new dataframe 
    df = pd.concat([df, categories], axis=1, join='inner')
    
    return df 


def clean_data(df):
                        
    #drop duplicates from the dataframe
    df = df.drop_duplicates(keep=False)
    
    return df


def save_data(df, database_filename):
    '''
    engine  point to database location
    df  upload and replace data into category_message database
    '''
    
    engine = create_engine('sqlite:///' + database_filename) 
    df = df.to_sql('category_message', engine, index=False, if_exists='replace')
    
    return df


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()

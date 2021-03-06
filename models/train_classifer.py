import sys

import pandas as pd
import numpy as np
import pickle 

import nltk
nltk.download(['punkt', 'wordnet'])
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sqlalchemy import create_engine 

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV


def load_data(database_filepath):
    '''
    Load data from the database 
    
    Arguments:
    database_filepath   Path to SQLite desitination database (i.e., category_message database)
    
    Outputs: 
    X   dataframe containing feature 
    Y   dataframe containing labels
    category_names  List of column names
    '''
    
    engine = create_engine('sqlite:///' + database_filepath)
    df = pd.read_sql_table('category_message', engine)
    
    X = df['message']
    Y = df.iloc[:, 4:]
    category_names = list(df.columns[4:])
    
    return X, Y, category_names


def tokenize(text):
    
    #tokenize text
    tokens = word_tokenize(text)
    
    #remove stop words
    tokens = [tok for tok in tokens if tok not in stop_words] 
    
    #lemmatize text
    lemmatizer = WordNetLemmatizer()
    
    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)
    
    return clean_tokens


def build_model():
    
    #set ML pipeline
    pipeline = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))])
    
    #use grid search to find better parameters
    parameters = {
        #'vect__ngram_range': ((1,1), (1,2))} 
        'vect__max_df': (0.75, 1.0)}
        # 'tfidf__use_idf': (True, False)}
    
    cv = GridSearchCV(pipeline, param_grid=parameters)
    
    return cv 


def evaluate_model(model, X_test, Y_test, category_names):
    
    Y_pred = model.predict(X_test)
    # col_names = list(Y.columns.values)
    
    for i in range(len(category_names)):
        print("Precision, Recall, F1 score for {}".format(category_names[i]))
        print(classification_report(Y_test.iloc[:, i], Y_pred[:, i]))
        
  

def save_model(model, model_filepath):
    pickle.dump(model, open('RFC_model.pkl', 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()

from data_upload import load_data
from pre_processing import preprocess_data
from train import train_model
import pandas as pd
import os



def main():
    print("\n")
    '''
    This is a data loading module that imports the load_data function from data_upload.py
    '''

    # Get the absolute path of the data file
    #---------------- If path related error occurs check this ------------------

    print("-"*10,end="")
    print("Data Loading Module initiating",end="")
    print("-"*10)
    print("\n")

    base_path = os.path.dirname(__file__)
    parent_path = os.path.join(base_path, "..","data_set","data1.csv")
    parent_path = os.path.abspath(parent_path)   # convert to absolute path
    print(f"Using data file at: {parent_path}\n")


    data = load_data(parent_path)
    print(data.head(2))
    print("\n")

    '''
    This is a pre-processing module that will handle data cleaning and transformation
    '''
    
    print("-"*10,end="")
    print("Data Pre-processing Module initiating",end="")
    print("-"*10)
    print("\n")
    
    X_train, X_test, y_train, y_test = preprocess_data(data)

    '''
    This is a model training module that will train the model and evaluate it
    '''
    print("-"*10,end="")
    print("Model Training Module initiating",end="")
    print("-"*10)
    print("\n")

    train_model(X_train, X_test, y_train, y_test)

if __name__ == "__main__":
    main()
import pandas as pd
from feature_operation import feature_operation
from sklearn.model_selection import train_test_split

def preprocess_data(data):
    """
    Preprocess the input data by handling missing values and encoding categorical variables.

    Parameters:
    data (pd.DataFrame): The input data to preprocess.

    Returns:
    pd.DataFrame: The preprocessed data.
    """
    
    # check for data intigrity 
    j = 0
    columns_handel = list()
    for i in data.columns:
        if data[i].isnull().sum()>0:
            j += 1
            print(f"{j}. Column {i} has {data[i].isnull().sum()} {data[i].isnull().sum()/len(data)*100:.2f}% missing values.")
            columns_handel.append(i)
    print("\n")

    # remove row for column where price is missing since its our target variable
    prev_shape = data.shape
    if 'price' in columns_handel:
        # df.method({col: value}, inplace=True)
        data = data[~data['price'].isnull()]
        columns_handel.remove('price')
        print(f"Removed rows with missing Price values. Prev to New data shape: {prev_shape} -> {data.shape}\n")

    # Handling missing values
    data = data.copy()   # 🔥 fixes SettingWithCopyWarning

    for col in columns_handel:
        if data[col].dtype == 'object':
            mode_val = data[col].mode()[0]
            data.loc[:, col] = data[col].fillna(mode_val)
            print(f"Filled missing values in {col} with mode: {mode_val}\n")

        else:
            skew_val = data[col].skew()
            
            if abs(skew_val) > 0.5:
                mean_val = data[col].mean()
                data.loc[:, col] = data[col].fillna(mean_val)
                print(f"Filled missing values in {col} with mean due to skewness of {skew_val:.2f}\n")
            else:
                median_val = data[col].median()
                data.loc[:, col] = data[col].fillna(median_val)
                print(f"Filled missing values in {col} with median due to skewness of {skew_val:.2f}\n")
    # data type conversion

    print("Data types before conversion:\n")
    print(data.info())

    data['start_date'] = pd.to_datetime(data['start_date'])
    data['end_date'] = pd.to_datetime(data['end_date'])
    data['insert_date'] = pd.to_datetime(data['insert_date'])

    print("Data types after conversion:\n")
    print(data.info())
    
    '''
    This is a feature engineering module that will create new features and feature operations
    '''
    print("-"*10,end="")
    print("Feature Engineering Module initiating",end="")
    print("-"*10)
    print("\n")

    featured_data = feature_operation(data)
    print(featured_data.head(2))

    print("\n")
    print(featured_data.info())
    print("\n")
    print(featured_data.describe().T)
    print("\n")

    # split features and target variable

    # Target variable
    y = featured_data['price']

    # Feature variables (all columns except price)
    X = featured_data.drop(columns=['price'])

    # final dataset columns order and choosen
    print(X.columns)
    print("\n")

    # Train 70% / Test 30%
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=42
    )

    print("X_train shape:", X_train.shape)
    print("X_test shape:", X_test.shape)
    print("y_train shape:", y_train.shape)
    print("y_test shape:", y_test.shape)
    
    return X_train, X_test, y_train, y_test
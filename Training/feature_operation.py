import pandas as pd
import joblib
import os
from sklearn.preprocessing import LabelEncoder

def feature_operation(data):
    """
    Perform feature engineering operations on the dataset.

    Args:
    data (pd.DataFrame): The input data.

    Returns:
    pd.DataFrame: The data with new features added.
    """
    
    # remove first column 'Unnamed: 0' from data
    if 'Unnamed: 0' in data.columns:
        data = data.drop(columns=['Unnamed: 0'])
        print("Dropped column 'Unnamed: 0'\n")
    
    # add new feature: total_hour : the train duration in hours
    data = data.copy()   # 🔥 fixes SettingWithCopyWarning

    data['total_hour'] = (data['end_date'] - data['start_date']) / pd.Timedelta(hours=1)
    print("Added new feature 'total_hour'\n")

    # add new feature: To_journey_hour : booking to journey start hour
    data['To_journey_hour'] = (data['start_date'] - data['insert_date']) / pd.Timedelta(hours=1)
    print("Added new feature 'To_journey_hour'\n")

    # add new feature: is_luxury_class : binary feature indicating if the train class is luxury
    luxury_classes = ["Preferente", "Turista Plus", "Cama Turista"]
    data["is_luxury_class"] = data["train_class"].isin(luxury_classes).astype(int)
    print("Added new feature 'is_luxury_class'\n")

    # add new feature: fare_score : numerical score for fare types
    fare_score_map = {"Flexible": 2, "Promo +": 1, "Promo": 0, "Adulto ida": 0, "Mesa": 0}
    data["fare_score"] = data["fare"].map(fare_score_map)
    print("Added new feature 'fare_score'\n")

    # drop columns not required for modeling
    cols_to_drop = ['insert_date', 'start_date', 'end_date',]
    data = data.drop(columns=cols_to_drop)
    print(f"Dropped columns: {cols_to_drop}\n")

    # label encoding for categorical features
    
    categorical_cols = ['train_type', 'train_class', 'fare','origin', 'destination']

    label_encoders = {}  # dict: column_name -> LabelEncoder
    for col in categorical_cols:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])
        label_encoders[col] = le          # store encoder for that column
        print(f"Label encoded column: {col}")

    # save the dict of encoders
    model_dir = os.path.join(os.path.dirname(__file__), "..", "artifacts", "transformers")
    model_dir = os.path.abspath(model_dir)
    os.makedirs(model_dir, exist_ok=True)

    label_encoders_path = os.path.join(model_dir, "label_encoders.joblib")
    joblib.dump(label_encoders, label_encoders_path)

    print(f"Saved LabelEncoders dict at: {label_encoders_path}")

    # reset index
    data = data.reset_index(drop=True)
    data.drop(columns=['index'], errors='ignore', inplace=True)

    print(f"Final columns after feature operations: {data.columns.tolist()}\n")

    print("Feature engineering operations completed.\n")

    return data
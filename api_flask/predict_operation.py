import pandas as pd
import numpy as np

def predict_price(input_data, model, label_encoders):
    """
    Predict the train ticket price based on input data using the provided model and label encoders.

    Parameters:
    - input_data (dict): A dictionary containing the input features for prediction.
    - model: The trained machine learning model for prediction.
    - label_encoders (dict): A dictionary of label encoders for categorical features.

    Returns:
    - float: The predicted ticket price.
    """
    """
    data = {
            'insert_date': insert_date,
            'origin': origin,
            'destination': destination,
            'start_date': start_date,
            'end_date': end_date,
            'train_type': train_type,
            'price': price,
            'train_class': train_class,
            'fare': fare
        }
    """

    # Convert input data to DataFrame
    print("Input data for prediction:\n", input_data)
    input_df = pd.DataFrame([input_data])
    print("Input DataFrame for prediction:\n", input_df)
    # date feature engineering
    input_df['insert_date'] = pd.to_datetime(input_df['insert_date'])
    input_df['start_date'] = pd.to_datetime(input_df['start_date'])
    input_df['end_date'] = pd.to_datetime(input_df['end_date'])

    input_df['total_hour'] = (input_df['end_date'] - input_df['start_date']) / pd.Timedelta(hours=1)
    input_df['To_journey_hour'] = (input_df['start_date'] - input_df['insert_date']) / pd.Timedelta(hours=1)

    luxury_classes = ["Preferente", "Turista Plus", "Cama Turista"]
    input_df["is_luxury_class"] = input_df["train_class"].isin(luxury_classes).astype(int)

    fare_score_map = {"Flexible": 2, "Promo +": 1, "Promo": 0, "Adulto ida": 0, "Mesa": 0}
    input_df["fare_score"] = input_df["fare"].map(fare_score_map)

    cols_to_drop = ['insert_date', 'start_date', 'end_date',]
    input_df = input_df.drop(columns=cols_to_drop)

    categorical_cols = ['train_type', 'train_class', 'fare','origin', 'destination']

    for col in categorical_cols:
        le = label_encoders[col]
        input_df[col] = le.transform(input_df[col])

    # order the columns as per training data if required
    """ ['origin', 'destination', 'train_type', 'train_class', 'fare',
       'total_hour', 'To_journey_hour', 'is_luxury_class', 'fare_score']
    """
    input_df = input_df[['origin', 'destination', 'train_type', 'train_class', 'fare',
                         'total_hour', 'To_journey_hour', 'is_luxury_class', 'fare_score']]

    # Predict using the model
    print("Input DataFrame after feature engineering for prediction:\n", input_df)
    predicted_price = model.predict(input_df)
    return float(predicted_price[0])
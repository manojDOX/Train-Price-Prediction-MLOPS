from lightgbm import LGBMRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import os
import json
import joblib
from sklearn.model_selection import RandomizedSearchCV

def train_model(X_train, X_test, y_train, y_test):
    # base model performance without hyperparameter tuning

    base_model_LGBMR = LGBMRegressor(random_state=42)
    base_model_LGBMR.fit(X_train, y_train)
    y_pred = base_model_LGBMR.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse}")
    print(f"R^2 Score: {r2}")

    # residule plot
    residuals = y_test - y_pred
    plt.figure(figsize=(10, 6))
    plt.scatter(y_pred, residuals)
    plt.axhline(y=0, color='r', linestyle='--')
    plt.xlabel('Predicted Values')
    plt.ylabel('Residuals')
    plt.title('Residual Plot')


    # save image of residule plot in artifacts/images folder
    image_dir = os.path.join(os.path.dirname(__file__), "..", "artifacts", "images")
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    image_path = os.path.join(image_dir, "residual_plot.png")
    plt.savefig(image_path)
    plt.show()

    # save as json file the model performance metrics in artifacts/metrics folder
    metrics_dir = os.path.join(os.path.dirname(__file__), "..", "artifacts", "metrics")
    if not os.path.exists(metrics_dir):
        os.makedirs(metrics_dir)
    metrics_path = os.path.join(metrics_dir, "model_performance.json")
    with open(metrics_path, "w") as f:
        json.dump({"mean_squared_error": mse, "r2_score": r2}, f)

    print(f"Saved residual plot at: {image_path}")
    print(f"Saved model performance metrics at: {metrics_path}\n")

    # save the trained model in artifacts/models folder
    model_dir = os.path.join(os.path.dirname(__file__), "..", "artifacts", "models")
    if not os.path.exists(model_dir):   
        os.makedirs(model_dir)
    model_path = os.path.join(model_dir, "lgbm_regressor_model.joblib")
    joblib.dump(base_model_LGBMR, model_path)
    print(f"Saved trained model at: {model_path}")

    # Hyperparameter tuning for the LGBMRegressor model
    hyper_model_LGBMR = LGBMRegressor(random_state=42)
    param_dist_lgbm = {
        "n_estimators": [200, 500, 800],            # number of boosting rounds
        "learning_rate": [0.01, 0.03, 0.05, 0.1],   # step size shrinkage
        "num_leaves": [31, 63, 127, 255],           # controls model complexity
        "max_depth": [-1, 5, 10, 15],               # -1 means no limit
        "min_child_samples": [5, 10, 20, 30],       # similar to min_samples_leaf
        "subsample": [0.6, 0.8, 1.0],               # aka bagging fraction
        "colsample_bytree": [0.6, 0.8, 1.0],        # feature sampling like max_features
        "reg_lambda": [0, 1, 5, 10],                # L2 regularization
        "reg_alpha": [0, 1, 5],                     # L1 regularization
    }
    random_search_lgbm = RandomizedSearchCV(
        estimator=hyper_model_LGBMR,
        param_distributions=param_dist_lgbm,
        n_iter=50,                # number of parameter settings sampled
        scoring='neg_mean_squared_error',
        cv=3,                     # 3-fold cross-validation
        verbose=10,
        random_state=42,
        n_jobs=-1                 # use all available cores
    )
    random_search_lgbm.fit(X_train, y_train)
    best_model_lgbm = random_search_lgbm.best_estimator_
    y_pred_hyper = best_model_lgbm.predict(X_test)
    mse_hyper = mean_squared_error(y_test, y_pred_hyper)
    r2_hyper = r2_score(y_test, y_pred_hyper)
    print(f"After Hyperparameter Tuning - Mean Squared Error: {mse_hyper}")
    print(f"After Hyperparameter Tuning - R^2 Score: {r2_hyper}")

    # save the hyperparameter tuned model in artifacts/models folder
    hyper_model_path = os.path.join(model_dir, "lgbm_regressor_hyper_model.joblib")
    joblib.dump(best_model_lgbm, hyper_model_path)
    print(f"Saved hyperparameter tuned model at: {hyper_model_path}")
    # save as json file the hyperparameter tuned model performance metrics in artifacts/metrics folder
    hyper_metrics_path = os.path.join(metrics_dir, "hyper_model_performance.json")
    with open(hyper_metrics_path, "w") as f:
        json.dump({"mean_squared_error": mse_hyper, "r2_score": r2_hyper}, f)
    print(f"Saved hyperparameter tuned model performance metrics at: {hyper_metrics_path}")

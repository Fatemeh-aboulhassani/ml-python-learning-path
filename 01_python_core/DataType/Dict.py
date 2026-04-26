# %% [markdown]
# # Python Core — Dictionaries
#
# ## Section 1 — Complete Lesson
#
# A dictionary stores data as key-value pairs.
#
# Dictionaries are important in Python because we use them for:
#
# - user profiles
# - API responses
# - model configurations
# - dataset metadata
# - feature records
# - preprocessing reports
# - JSON-like data
# - structured project data
#
# Main properties:
#
# - key-value based
# - mutable
# - ordered in modern Python
# - keys must be unique
# - values can be any type
# - very common in real projects
#
# Core syntax:
#
# ```python
# user = {
#     "name": "Ali",
#     "age": 25,
#     "is_active": True
# }
#
# empty_dict = {}
#
# user["name"]              # access value
# user.get("name")          # safe access
# user.get("city", "N/A")   # default value
#
# user["age"] = 26          # update value
# user["city"] = "Tehran"   # add new key-value pair
#
# del user["age"]           # delete by key
# removed = user.pop("city")
# user.clear()
#
# "name" in user
# "email" not in user
#
# len(user)
#
# user.keys()
# user.values()
# user.items()
#
# for key in user:
#     print(key)
#
# for key, value in user.items():
#     print(key, value)
#
# user_copy = user.copy()
#
# config.update({
#     "epochs": 20,
#     "batch_size": 32
# })
#
# nested_dict = {
#     "model": {
#         "name": "RandomForest",
#         "accuracy": 0.93
#     }
# }
#
# nested_dict["model"]["accuracy"]
# ```
#
# Important notes:
#
# - Use clear key names: `"model_name"`, `"accuracy"`, `"target_column"`
# - Use `.get()` when a key may not exist
# - Use `.copy()` when you need a real copy
# - Dictionary keys are unique
# - Updating an existing key replaces its old value
# - Dictionaries are the base idea behind JSON and many API responses
# - In ML, dictionaries are useful for configs, metrics, feature records, and reports


# %% [markdown]
# ## Exercise 1 — Dataset Metadata Dictionary
#
# Create a dictionary for dataset metadata.
#
# Required keys:
#
# - dataset_name
# - rows
# - columns
# - target_column
# - missing_values
# - is_cleaned
#
# Tasks:
#
# - print the dataset name
# - print number of rows and columns
# - print whether the dataset is cleaned
# - add a new key named `source`
# - update `is_cleaned` to `True`
# - print a clean dataset report
#
# Goal:
#
# Practice creating, accessing, adding, updating, and reporting dictionary data.

# %%
dataset_info = {
    "dataset_name": "Customer Churn",
    "rows": 10000,
    "columns": 24,
    "target_column": "churn",
    "missing_values": 135,
    "is_cleaned": False
}

# write your code here


# %% [markdown]
# ## Exercise 2 — ML Model Configuration
#
# You have a model configuration dictionary.
#
# Tasks:
#
# - access model name
# - update learning rate
# - add `early_stopping`
# - add `random_state`
# - print all keys
# - print all values
# - print the final configuration
#
# Goal:
#
# Practice updating ML configuration dictionaries.

# %%
model_config = {
    "model_name": "Neural Network",
    "learning_rate": 0.01,
    "epochs": 20,
    "batch_size": 32,
    "optimizer": "adam"
}

# write your code here


# %% [markdown]
# ## Exercise 3 — Model Metrics Report
#
# You have model evaluation metrics.
#
# Tasks:
#
# - calculate average of accuracy, precision, recall, and f1_score
# - add the result as `average_score`
# - print each metric as percentage with 2 decimal places
# - print a final model report
#
# Goal:
#
# Practice numeric values inside dictionaries and ML-style reporting.

# %%
metrics = {
    "accuracy": 0.92,
    "precision": 0.89,
    "recall": 0.87,
    "f1_score": 0.88
}

# write your code here


# %% [markdown]
# ## Exercise 4 — Safe API Response Reading
#
# You have an API response dictionary.
#
# Tasks:
#
# - safely read `status`
# - safely read `message`
# - safely read `user_id`
# - safely read `email`
# - safely read a missing key named `phone` with default value `"Not provided"`
# - print a clean API response report
#
# Goal:
#
# Practice `.get()` and nested dictionary access.

# %%
api_response = {
    "status": "success",
    "message": "User loaded successfully",
    "data": {
        "user_id": 101,
        "username": "ai_student",
        "email": "student@example.com",
        "is_active": True
    }
}

# write your code here


# %% [markdown]
# ## Exercise 5 — Clean Feature Record
#
# You have one raw feature record for an ML model.
#
# Tasks:
#
# - replace missing age with `0`
# - replace missing income with `0`
# - convert `purchased` from `"yes"` to `1`
# - add a new key `is_valid`
# - `is_valid` should be True if age and income are greater than 0
# - print the cleaned record
#
# Goal:
#
# Practice dictionary cleaning and simple ML preprocessing logic.

# %%
record = {
    "age": None,
    "income": None,
    "city": "Berlin",
    "purchased": "yes"
}

# write your code here


# %% [markdown]
# ## Exercise 6 — Count Class Labels
#
# You have a list of class labels.
#
# Tasks:
#
# - create a dictionary that counts each label
# - print the final label count dictionary
# - print how many times `"cat"` appears
# - print how many unique labels exist
#
# Goal:
#
# Practice dictionaries for frequency counting, a common ML/data task.

# %%
labels = ["cat", "dog", "cat", "car", "dog", "cat", "person", "car", "dog"]

# write your code here


# %% [markdown]
# ## Exercise 7 — Hyperparameter Search Results
#
# You have results from several model experiments.
#
# Each key is an experiment name.
# Each value is model accuracy.
#
# Tasks:
#
# - find the best experiment name
# - find the best accuracy
# - find the worst experiment name
# - find the worst accuracy
# - create a dictionary of experiments with accuracy >= 0.90
# - print a clean experiment report
#
# Goal:
#
# Practice dictionary iteration and ML experiment analysis.

# %%
experiment_results = {
    "exp_01": 0.84,
    "exp_02": 0.91,
    "exp_03": 0.88,
    "exp_04": 0.94,
    "exp_05": 0.89,
    "exp_06": 0.92
}

# write your code here


# %% [markdown]
# ## Exercise 8 — Nested Dictionary: Training Run Report
#
# You have a nested dictionary for a training run.
#
# Tasks:
#
# - access model name
# - access dataset name
# - access train accuracy
# - access validation accuracy
# - calculate overfitting gap:
#
# ```python
# train_accuracy - validation_accuracy
# ```
#
# - add `overfitting_gap` inside the `metrics` dictionary
# - print a professional training report
#
# Goal:
#
# Practice nested dictionary access and ML reporting.

# %%
training_run = {
    "model": {
        "name": "Random Forest",
        "version": "1.0"
    },
    "dataset": {
        "name": "Customer Churn",
        "rows": 10000
    },
    "metrics": {
        "train_accuracy": 0.97,
        "validation_accuracy": 0.89
    }
}

# write your code here


# %% [markdown]
# ## Exercise 9 — Feature Validation Report
#
# You have expected feature names and received feature values.
#
# Tasks:
#
# - check if all required features exist in the input record
# - create a list of missing features
# - create a dictionary named `validation_report`
# - validation report should contain:
#
#   - total_required_features
#   - total_received_features
#   - missing_features
#   - is_valid
#
# - print the validation report
#
# Goal:
#
# Practice dictionaries in ML input validation.

# %%
required_features = ["age", "income", "credit_score", "employment_years"]

input_record = {
    "age": 35,
    "income": 72000,
    "credit_score": 690
}

# write your code here


# %% [markdown]
# ## Exercise 10 — Final Project: ML Experiment Tracker
#
# You are building a small ML experiment tracker.
#
# You have a dictionary where each experiment has:
#
# - model name
# - accuracy
# - precision
# - recall
# - training time
#
# Tasks:
#
# - calculate average score for each experiment:
#
# ```python
# average_score = (accuracy + precision + recall) / 3
# ```
#
# - add `average_score` to each experiment
# - find the best experiment based on average score
# - find the fastest experiment based on training time
# - create a final summary dictionary with:
#
#   - best_experiment
#   - best_average_score
#   - fastest_experiment
#   - fastest_training_time
#   - total_experiments
#
# - print a professional experiment tracking report
#
# Goal:
#
# Combine nested dictionaries, loops, updates, metrics, and reporting.

# %%
experiments = {
    "exp_01": {
        "model_name": "Logistic Regression",
        "accuracy": 0.86,
        "precision": 0.84,
        "recall": 0.82,
        "training_time": 12.5
    },
    "exp_02": {
        "model_name": "Random Forest",
        "accuracy": 0.91,
        "precision": 0.89,
        "recall": 0.88,
        "training_time": 45.2
    },
    "exp_03": {
        "model_name": "XGBoost",
        "accuracy": 0.93,
        "precision": 0.91,
        "recall": 0.90,
        "training_time": 61.8
    },
    "exp_04": {
        "model_name": "SVM",
        "accuracy": 0.88,
        "precision": 0.87,
        "recall": 0.85,
        "training_time": 38.4
    }
}

# write your code here
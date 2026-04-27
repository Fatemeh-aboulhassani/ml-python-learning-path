

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

print(dataset_info["dataset_name"])
print(dataset_info["rows"], dataset_info["columns"])
print(dataset_info["is_cleaned"])

dataset_info["source"] = "Kaggle"
dataset_info["is_cleaned"] = True

print(dataset_info)

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

print(model_config["model_name"])

model_config["learning_rate"] = 0.001
model_config["early_stopping"] = True
model_config["random_state"] = 42

print(model_config.keys())
print(model_config.values())
print(model_config)


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

avg = sum(metrics.values()) / len(metrics)
metrics["average_score"] = avg

for k, v in metrics.items():
    print(f"{k}: {v*100:.2f}%")

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

print(api_response.get("status"))
print(api_response.get("message"))

data = api_response.get("data", {})
print(data.get("user_id"))
print(data.get("email"))
print(data.get("phone", "Not provided"))


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

record["age"] = record["age"] or 0
record["income"] = record["income"] or 0
record["purchased"] = 1 if record["purchased"] == "yes" else 0

record["is_valid"] = record["age"] > 0 and record["income"] > 0

print(record)



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

count_dict = {}

for label in labels:
    count_dict[label] = count_dict.get(label, 0) + 1

print(count_dict)
print(count_dict.get("cat"))
print(len(count_dict))

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

best_exp = max(experiment_results, key=experiment_results.get)
worst_exp = min(experiment_results, key=experiment_results.get)

high_perf = {k: v for k, v in experiment_results.items() if v >= 0.90}

print(best_exp, experiment_results[best_exp])
print(worst_exp, experiment_results[worst_exp])
print(high_perf)




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

train_acc = training_run["metrics"]["train_accuracy"]
val_acc = training_run["metrics"]["validation_accuracy"]

gap = train_acc - val_acc
training_run["metrics"]["overfitting_gap"] = gap

print(training_run)


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

missing = [f for f in required_features if f not in input_record]

report = {
    "total_required_features": len(required_features),
    "total_received_features": len(input_record),
    "missing_features": missing,
    "is_valid": len(missing) == 0
}

print(report)



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

best_exp = None
best_score = 0
fastest_exp = None
fastest_time = float("inf")

for name, data in experiments.items():
    avg = (data["accuracy"] + data["precision"] + data["recall"]) / 3
    data["average_score"] = avg

    if avg > best_score:
        best_score = avg
        best_exp = name

    if data["training_time"] < fastest_time:
        fastest_time = data["training_time"]
        fastest_exp = name

summary = {
    "best_experiment": best_exp,
    "best_average_score": best_score,
    "fastest_experiment": fastest_exp,
    "fastest_training_time": fastest_time,
    "total_experiments": len(experiments)
}

print(summary)
# %%

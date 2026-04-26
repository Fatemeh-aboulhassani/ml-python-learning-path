
# %% [markdown]
# ## Exercise 1 — Clean Sensor Data for ML
#
# You have raw sensor readings.
#
# Invalid values:
#
# - negative numbers
# - `9999`
#
# Tasks:
#
# - create a clean list with only valid readings
# - count raw readings
# - count valid readings
# - count invalid readings
# - calculate average valid reading
# - find minimum valid reading
# - find maximum valid reading
# - print a clean report
#
# Goal:
#
# Practice filtering, list comprehension, numeric operations, and reporting.

# %%


clean_readings = [value for value in readings if value >= 0 and value != 9999]

raw_count = len(readings)
valid_count = len(clean_readings)
invalid_count = raw_count - valid_count
average_reading = sum(clean_readings) / valid_count
min_reading = min(clean_readings)
max_reading = max(clean_readings)

print("Sensor Data Report")
print("------------------")
print(f"Raw readings: {raw_count}")
print(f"Valid readings: {valid_count}")
print(f"Invalid readings: {invalid_count}")
print(f"Average: {average_reading:.2f}")
print(f"Min: {min_reading}")
print(f"Max: {max_reading}")




# %% [markdown]
# ## Exercise 2 — Normalize Feature Values
#
# You have numeric feature values for a simple ML model.
#
# Normalization rule:
#
# ```python
# normalized_value = value / max_value
# ```
#
# Tasks:
#
# - find the maximum value
# - create a normalized list
# - print original values
# - print normalized values
# - print each normalized value with 3 decimal places
#
# Goal:
#
# Practice feature scaling logic before NumPy and Pandas.

# %%
feature_values = [120, 300, 250, 400, 150, 500]

max_value = max(feature_values)
normalized_values = [value/max_value for value in feature_values]

print("Feature Normalization Report")
print("----------------------------")
print(f"Original values: {feature_values}")
print(f"Max value: {max_value}")
print(f"Normalized values: {normalized_values}")

for value in normalized_values :
    print(f"{value:.3f}")


# %% [markdown]
# ## Exercise 3 — Model Accuracy Analyzer
#
# You trained several models and stored their accuracy scores.
#
# Tasks:
#
# - calculate best accuracy
# - calculate worst accuracy
# - calculate average accuracy
# - count models with accuracy >= 0.90
# - create a list of high-performing accuracies
# - print all results as percentages with 2 decimal places
#
# Goal:
#
# Practice list filtering and ML metric analysis.

# %%
accuracies = [0.82, 0.91, 0.88, 0.94, 0.79, 0.90, 0.96]

best_accuracy = max(accuracies)
worst_accuracy = min(accuracies)
average_accuracy = sum(accuracies) / len(accuracies)

high_performing_accuracies = [acc for acc in accuracies if acc>=0.90]
high_performing_count = len(high_performing_accuracies)

print("Model Accuracy Report")
print("---------------------")
print(f"Best accuracy:{best_accuracy*100:.2f}%")
print(f"Worst accuracy:{worst_accuracy*100:.2f}%")
print(f"Average accuracy :{average_accuracy*100:.2f}%")
print(f"High-performing models: {high_performing_count}")
print(f"High-performing accuracies: {[round(acc*100 , 2) for acc in high_performing_accuracies]}")



# %% [markdown]
# ## Exercise 4 — Clean Text Labels
#
# You have messy class labels from a dataset.
#
# Tasks:
#
# - remove extra spaces
# - convert all labels to lowercase
# - remove empty labels
# - remove duplicate labels while keeping order
# - print the final cleaned label list
#
# Goal:
#
# Practice text cleaning for dataset labels.

# %%
raw_labels = [" Cat ", "dog", "DOG ", " car", "", "cat", " Person ", "person", "  "]

clean_labels = []

for label in raw_labels:
    cleaned_label = label.strip().lower()

    if cleaned_label != "" and cleaned_label not in clean_labels:
        clean_labels.append(cleaned_label)

print("Clean Label Report")
print("------------------")
print(f"Raw labels: {raw_labels}")
print(f"Clean labels: {clean_labels}")



# %% [markdown]
# ## Exercise 5 — Train/Test Split Manually
#
# You have a small dataset represented as a list.
#
# Tasks:
#
# - split the data manually into 80% train and 20% test
# - do not use any library
# - calculate the split index
# - create `train_data`
# - create `test_data`
# - print both lists
# - print their lengths
#
# Goal:
#
# Understand dataset splitting before using scikit-learn.

# %%
data = [12, 15, 18, 21, 24, 30, 33, 36, 40, 45]

split_index = int(len(data) * 0.8)

train_data = data[:split_index]
test_data = data[split_index:]

print("Manual Train/Test Split Report")
print("------------------------------")
print(f"Full data: {data}")
print(f"Split index: {split_index}")
print(f"Train data: {train_data}")
print(f"Test data: {test_data}")
print(f"Train length: {len(train_data)}")
print(f"Test length: {len(test_data)}")

# %% [markdown]
# ## Exercise 6 — Outlier Detection with Mean
#
# You have numeric values.
#
# A value is suspicious if it is greater than 2 times the average.
#
# Tasks:
#
# - calculate the average
# - create a list of normal values
# - create a list of suspicious values
# - print average, normal values, and suspicious values
#
# Goal:
#
# Practice basic outlier detection logic using lists.

# %%
values = [10, 12, 11, 13, 500, 14, 9, 15, 600, 10]


values = [10, 12, 11, 13, 500, 14, 9, 15, 600, 10]

average_value = sum(values) / len(values)

normal_values = [value for value in values if value <= 2 * average_value]
suspicious_values = [value for value in values if value > 2 * average_value]

print("Outlier Detection Report")
print("------------------------")
print(f"Values: {values}")
print(f"Average: {average_value:.2f}")
print(f"Threshold: {2 * average_value:.2f}")
print(f"Normal values: {normal_values}")
print(f"Suspicious values: {suspicious_values}")

# %% [markdown]
# ## Exercise 7 — Batch Prediction Post-processing
#
# A model returned prediction probabilities.
#
# Rule:
#
# - probability >= 0.5 means class `1`
# - probability < 0.5 means class `0`
#
# Tasks:
#
# - create a list of predicted labels
# - count class `1` predictions
# - count class `0` predictions
# - print a prediction summary
#
# Goal:
#
# Practice converting model outputs into usable labels.

# %%
probabilities = [0.91, 0.12, 0.55, 0.49, 0.80, 0.33, 0.67, 0.20]

predicted_labels = [1 if probability >= 0.5 else 0 for probability in probabilities]

class_1_count = predicted_labels.count(1)
class_0_count = predicted_labels.count(0)

print("Prediction Summary")
print("------------------")
print(f"Probabilities: {probabilities}")
print(f"Predicted labels: {predicted_labels}")
print(f"Class 1 count: {class_1_count}")
print(f"Class 0 count: {class_0_count}")

# write your code here


# %% [markdown]
# ## Exercise 8 — API Latency Analysis
#
# You have backend API response times in milliseconds.
#
# Tasks:
#
# - calculate average latency
# - find fastest request
# - find slowest request
# - create a list of slow requests above 200 ms
# - calculate percentage of slow requests
# - print a clean backend performance report
#
# Goal:
#
# Practice real-world list analysis used in web systems.

# %%
response_times = [120, 95, 210, 180, 305, 150, 260, 110, 400, 170]

average_latency = sum(response_times) / len(response_times)
fastest_request = min(response_times)
slowest_request = max(response_times)

slow_requests = [time for time in response_times if time > 200]
slow_request_percentage = len(slow_requests) / len(response_times) * 100

print("API Latency Report")
print("------------------")
print(f"Response times: {response_times}")
print(f"Average latency: {average_latency:.2f} ms")
print(f"Fastest request: {fastest_request} ms")
print(f"Slowest request: {slowest_request} ms")
print(f"Slow requests: {slow_requests}")
print(f"Slow request percentage: {slow_request_percentage:.2f}%")


# %% [markdown]
# ## Exercise 9 — Nested List Dataset Processing
#
# You have a simple dataset.
#
# Each row is:
#
# ```python
# [age, income, purchased]
# ```
#
# Tasks:
#
# - extract all ages into a list
# - extract all incomes into a list
# - extract all labels into a list
# - calculate average age
# - calculate average income
# - count how many users purchased
# - print a dataset report
#
# Goal:
#
# Practice nested lists like simple tabular ML data.

# %%
dataset = [
    [25, 50000, 1],
    [32, 64000, 0],
    [47, 120000, 1],
    [22, 35000, 0],
    [36, 80000, 1],
]

dataset = [
    [25, 50000, 1],
    [32, 64000, 0],
    [47, 120000, 1],
    [22, 35000, 0],
    [36, 80000, 1],
]

ages = []
incomes = []
labels = []

for row in dataset:
    age = row[0]
    income = row[1]
    label = row[2]

    ages.append(age)
    incomes.append(income)
    labels.append(label)

average_age = sum(ages) / len(ages)
average_income = sum(incomes) / len(incomes)
purchased_count = labels.count(1)

print("Dataset Report")
print("--------------")
print(f"Ages: {ages}")
print(f"Incomes: {incomes}")
print(f"Labels: {labels}")
print(f"Average age: {average_age:.2f}")
print(f"Average income: {average_income:.2f}")
print(f"Purchased count: {purchased_count}")


# %% [markdown]
# ## Exercise 10 — Final Project: ML Data Preparation Pipeline
#
# You have raw numeric data for one feature column.
#
# Invalid values:
#
# - `None`
# - negative numbers
# - values greater than 1000
#
# Tasks:
#
# - create a clean list
# - count raw values
# - count removed values
# - sort the clean list without changing the original clean list
# - normalize clean values by dividing by max clean value
# - create a list of values above the average
# - print a professional preprocessing report
#
# Goal:
#
# Combine filtering, cleaning, copying, sorting, normalization, and reporting.

# %%
raw_feature = [120, 300, None, 250, -10, 400, 1500, 500, 180, None, 220]
clean_feature = []

for value in raw_feature:
    if isinstance(value, (int, float)) and value >= 0 and value <= 1000:
        clean_feature.append(value)
raw_count = len(raw_feature)
clean_count = len(clean_feature)
removed_count = raw_count - clean_count

sorted_clean_feature = sorted(clean_feature)

max_value = max(clean_feature)
normalized_feature = [value / max_value for value in clean_feature]

average_value = sum(clean_feature) / len(clean_feature)
above_average_values = [value for value in clean_feature if value > average_value]

print("ML Data Preparation Report")
print("--------------------------")
print(f"Raw feature: {raw_feature}")
print(f"Clean feature: {clean_feature}")
print(f"Raw count: {raw_count}")
print(f"Clean count: {clean_count}")
print(f"Removed count: {removed_count}")
print(f"Sorted clean feature: {sorted_clean_feature}")
print(f"Normalized feature: {[round(value, 3) for value in normalized_feature]}")
print(f"Average clean value: {average_value:.2f}")
print(f"Values above average: {above_average_values}")
# %%

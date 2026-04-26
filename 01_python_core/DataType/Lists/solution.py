# %% [markdown]
# # Python Core — Lists
#
# ## Section 1 — Complete Lesson
#
# A list stores multiple values in one variable.
#
# Lists are important in Python because we use them for:
#
# - data cleaning
# - feature values
# - labels
# - model scores
# - sensor readings
# - API results
# - batch processing
#
# Main properties:
#
# - ordered
# - mutable
# - index-based
# - iterable
# - allows duplicates
#
# Core syntax:
#
# ```python
# numbers = [10, 20, 30]
# empty_list = []
#
# numbers[0]        # first item
# numbers[-1]       # last item
# numbers[1:3]      # slicing
#
# numbers[0] = 100  # update
#
# numbers.append(40)
# numbers.insert(1, 15)
# numbers.extend([50, 60])
#
# numbers.remove(20)
# item = numbers.pop()
# item = numbers.pop(0)
# del numbers[0]
# numbers.clear()
#
# len(numbers)
# sum(numbers)
# min(numbers)
# max(numbers)
#
# 10 in numbers
# 99 not in numbers
#
# numbers.sort()
# sorted_numbers = sorted(numbers)
#
# numbers.reverse()
# reversed_numbers = numbers[::-1]
#
# numbers.count(10)
# numbers.index(10)
#
# copy_numbers = numbers.copy()
#
# for number in numbers:
#     print(number)
#
# for index, value in enumerate(numbers):
#     print(index, value)
#
# squares = [x ** 2 for x in numbers]
# valid_values = [x for x in numbers if x >= 0]
#
# matrix = [[1, 2], [3, 4]]
# matrix[0][1]
# ```
#
# Important notes:
#
# - Use plural names: `scores`, `prices`, `labels`
# - Use `.copy()` when you need a real copy
# - Use `sorted()` if you do not want to change the original list
# - Use `.sort()` if changing the original list is okay
# - Check existence before `remove()` or `index()`
# - Do not remove items from the same list while looping over it
# - In ML, lists are useful for small data, labels, features, scores, and preprocessing practice


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


# write your code here


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

# write your code here


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

# write your code here


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

# write your code here


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

# write your code here


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

# write your code here


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

# write your code here


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

# write your code here


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

# write your code here
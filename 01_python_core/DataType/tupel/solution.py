
# %% [markdown]
# ## Exercise 1 — Sensor Coordinate System
#
# You have 2D sensor coordinates.
#
# Tasks:
#
# - create a tuple (x, y)
# - print x and y separately
# - calculate distance from origin
#
# Goal:
#
# Practice tuple access + real math usage.

# %%
point = (3, 4)

x, y = point
distance = (x ** 2 + y ** 2) ** 0.5

print(f"x: {x}")
print(f"y: {y}")
print(f"Distance from origin: {distance:.2f}")


# %% [markdown]
# ## Exercise 2 — Model Output Structure
#
# Model returns:
#
# (prediction, confidence)
#
# Tasks:
#
# - unpack values
# - print both
# - check if confidence > 0.8
#
# Goal:
#
# Practice unpacking (very important in ML).

# %%
model_output = (1, 0.87)

prediction, confidence = model_output
is_confident = confidence > 0.8

print(f"Prediction: {prediction}")
print(f"Confidence: {confidence:.2f}")
print(f"Confident prediction: {is_confident}")


# %% [markdown]
# ## Exercise 3 — Dataset Row Processing
#
# Each row is:
#
# (age, income, purchased)
#
# Tasks:
#
# - unpack values
# - print each
# - convert purchased to bool
#
# Goal:
#
# Practice tuple as dataset row.

# %%
row = (35, 72000, 1)

age, income, purchased = row
purchased_bool = bool(purchased)

print(f"Age: {age}")
print(f"Income: {income}")
print(f"Purchased: {purchased_bool}")


# %% [markdown]
# ## Exercise 4 — Multiple Return Values Simulation
#
# Simulate a function returning multiple values:
#
# (mean, min, max)
#
# Tasks:
#
# - unpack values
# - print report
#
# Goal:
#
# Understand why tuples are used in functions.

# %%
stats = (22.5, 20.1, 25.3)

mean_value, min_value, max_value = stats

print("Statistics Report")
print("-----------------")
print(f"Mean: {mean_value}")
print(f"Min: {min_value}")
print(f"Max: {max_value}")


# %% [markdown]
# ## Exercise 5 — Tuple Immutability Test
#
# Try to change a value in a tuple.
#
# Then:
#
# - convert to list
# - modify value
# - convert back to tuple
#
# Goal:
#
# Understand immutability deeply.

# %%
data = (10, 20, 30)

# Tuple cannot be changed directly:
# data[0] = 100  # This would raise TypeError

data_list = list(data)
data_list[0] = 100
updated_data = tuple(data_list)

print(f"Original tuple: {data}")
print(f"Updated tuple: {updated_data}")

# %% [markdown]
# ## Exercise 6 — Feature & Label Split (ML)
#
# Dataset row:
#
# (features, label)
#
# Tasks:
#
# - unpack features and label
# - print features
# - print label
#
# Goal:
#
# Core ML data pattern.

# %%
sample = ((25, 72000, 680), 1)

features, label = sample

print(f"Features: {features}")
print(f"Label: {label}")


# %% [markdown]
# ## Exercise 7 — Batch Dataset Processing
#
# You have dataset:
#
# tuple of rows
#
# Tasks:
#
# - loop over dataset
# - extract all ages
# - extract all labels
# - calculate average age
#
# Goal:
#
# Tuple + loop + ML dataset logic.

# %%
dataset = (
    (25, 50000, 1),
    (32, 64000, 0),
    (47, 120000, 1),
    (22, 35000, 0)
)

ages = []
labels = []

for age, income, label in dataset:
    ages.append(age)
    labels.append(label)

average_age = sum(ages) / len(ages)

print(f"Ages: {ages}")
print(f"Labels: {labels}")
print(f"Average age: {average_age:.2f}")


# write your code here


# %% [markdown]
# ## Exercise 8 — Using Tuple as Dictionary Key
#
# Create dictionary:
#
# key = (x, y)
# value = label
#
# Tasks:
#
# - create at least 3 entries
# - access one value
# - print dictionary
#
# Goal:
#
# Advanced concept (tuple hashable).

# %%
points = {
    (1, 2): "A",
    (3, 4): "B"
}

points[(5, 6)] = "C"

selected_label = points[(3, 4)]

print(f"Selected point label: {selected_label}")
print(points)


# write your code here


# %% [markdown]
# ## Exercise 9 — Nested Tuple Metrics (ML)
#
# Structure:
#
# (
#   (accuracy, precision, recall),
#   (train_time, inference_time)
# )
#
# Tasks:
#
# - unpack everything
# - calculate average score
# - print report
#
# Goal:
#
# Deep tuple unpacking.

# %%
metrics = ((0.91, 0.89, 0.88), (45.2, 0.12))

(score_metrics, time_metrics) = metrics
accuracy, precision, recall = score_metrics
train_time, inference_time = time_metrics

average_score = (accuracy + precision + recall) / 3

print("Model Metrics Report")
print("--------------------")
print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"Precision: {precision * 100:.2f}%")
print(f"Recall: {recall * 100:.2f}%")
print(f"Average Score: {average_score * 100:.2f}%")
print(f"Train Time: {train_time:.2f}s")
print(f"Inference Time: {inference_time:.2f}s")

# %% [markdown]
# ## Exercise 10 — Final Project: Immutable ML Pipeline Config
#
# You have a tuple config:
#
# (
#   model_name,
#   (learning_rate, epochs),
#   (train_size, test_size)
# )
#
# Tasks:
#
# - unpack all values
# - print config
# - simulate updating learning_rate (using conversion)
# - rebuild tuple
# - print updated config
#
# Goal:
#
# Combine immutability + ML config + restructuring.

# %%
config = ("NeuralNet", (0.01, 20), (0.8, 0.2))

model_name, training_params, split_params = config
learning_rate, epochs = training_params
train_size, test_size = split_params

print("Original Config")
print("---------------")
print(f"Model: {model_name}")
print(f"Learning Rate: {learning_rate}")
print(f"Epochs: {epochs}")
print(f"Train Size: {train_size}")
print(f"Test Size: {test_size}")

# Simulate updating learning rate
new_learning_rate = 0.001
updated_config = (
    model_name,
    (new_learning_rate, epochs),
    (train_size, test_size)
)

print("\nUpdated Config")
print("--------------")
print(updated_config)
# %%

import pandas as pd
import numpy as np

# Question 1: Version of Pandas
print(pd.__version__)


# Question 2: Number of columns in the dataset
# Load the dataset
df = pd.read_csv('~/Downloads/Main-Algorithms/housing.csv')  # or any other method to load your dataset
# Get the number of columns
num_columns = df.shape[1]
print(f"There are {num_columns} columns in the dataset.")


# Question 3: Select columns with missing data
missing_cols = df.columns[df.isnull().any()]
print(f"There are {missing_cols} columns with missing data.")


# Question 4: Number of unique values in the 'ocean_proximity' column
# Assuming df is your DataFrame
unique_values = df['ocean_proximity'].unique()
num_unique_values = len(unique_values)
print(num_unique_values)


# Question 5: Average value of the 'median_house_value' for the houses near the bay
# Filter rows where location is near the bay
near_bay_df = df[df['ocean_proximity'] == 'NEAR BAY']
# Compute the average of the 'median_house_value' for those rows
average_value_near_bay = near_bay_df['median_house_value'].mean()
print(average_value_near_bay)


# Question 6: Has the mean value changed after filling missing values?
# Calculate the average of the 'total_bedrooms' column
average_total_bedrooms = df['total_bedrooms'].mean()
print(average_total_bedrooms)
# Fill missing values in 'total_bedrooms' with the mean value
df['total_bedrooms'].fillna(average_total_bedrooms, inplace=True)
# Recalculate the average of the 'total_bedrooms' column after filling NaN values
new_average_total_bedrooms = df['total_bedrooms'].mean()
print(new_average_total_bedrooms)


# Questions 7: Value of the last element of w
# Assuming 'ocean_proximity' (or similar) is the column indicating location
island_df = df[df['ocean_proximity'] == 'ISLAND']  # adjust as per your dataset
# 2. Select specific columns
selected_columns = island_df[['housing_median_age', 'total_rooms', 'total_bedrooms']]
# 3. Get the underlying NumPy array
X = selected_columns.values
print(X.shape)
# 4. Matrix multiplication between transpose of X and X
XTX = X.T.dot(X)
# 5. Compute the inverse of XTX
XTX_inv = np.linalg.inv(XTX)
# 6. Multiply the inverse of XTX with the transpose of X
XTX_inv_XT = XTX_inv.dot(X.T)
# Create an array y with given values
y = np.array([950, 1300, 800, 1000, 1300])
# Multiply the result by y
w = XTX_inv_XT.dot(y)
# Print the last element of w
print(w[-1])
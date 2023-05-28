import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


# Load the dataset
dataset_path = r"C:\Users\abhay\Downloads\titanic.csv"
data = pd.read_csv(dataset_path)

# Plot histogram of Age
plt.hist(data['Age'].dropna(), bins=20)
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Histogram of Age')
plt.show()

# Bar plot of survival rate based on gender
data.groupby('Sex')['Survived'].mean().plot(kind='bar')
plt.xlabel('Gender')
plt.ylabel('Survival Rate')
plt.title('Survival Rate based on Gender')
plt.xticks(rotation=0)
plt.show()

# Create correlation matrix
corr_matrix = data.corr()

# Plot correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Perform descriptive statistics
statistics = data.describe()
print(statistics)

# Fill missing values with column mean
data.fillna(data.mean(), inplace=True)

# Find outliers using IQR
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Replace outliers
data = data[(data >= lower_bound) & (data <= upper_bound)].dropna()

# Perform one-hot encoding on 'Sex' column
encoded_data = pd.get_dummies(data, columns=['Sex'])

# Split the data into dependent and independent variables
X = encoded_data.drop('Survived', axis=1)
y = encoded_data['Survived']

# Create a StandardScaler object
scaler = StandardScaler()

# Scale the independent variables (X)
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

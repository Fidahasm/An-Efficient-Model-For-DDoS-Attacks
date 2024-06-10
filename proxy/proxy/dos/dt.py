# Importing necessary libraries
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text
# Load iris dataset
iris = load_iris()
X = iris.data
y = iris.target
# Initialize decision tree classifier
clf = DecisionTreeClassifier()

# Fit the classifier on the data
clf.fit(X, y)

# Extracting important features
important_features = clf.feature_importances_

# Printing the importance of each feature
print("Feature Importance:")
for i, importance in enumerate(important_features):
    print(f"Feature {i+1}: {importance}")

# Displaying the decision tree rules
tree_rules = export_text(clf, feature_names=iris.feature_names)
print("\nDecision Tree Rules:")
print(tree_rules)

















#################################3

# # Importing necessary libraries
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score, classification_report
# import pandas as pd
#
# # Load your dataset
# # Assuming you have a CSV file named 'network_data.csv' with columns for features and a column named 'is_dos' indicating whether it's a DOS attack or not.
# data = pd.read_csv('network_data.csv')
#
# # Assuming 'X' contains features and 'y' contains target labels
# X = data.drop('is_dos', axis=1)  # Features
# y = data['is_dos']  # Target labels
#
# # Split the dataset into training and testing sets
# X_train, X_\test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # Initialize the Decision Tree classifier
# clf = DecisionTreeClassifier()
#
# # Train the classifier on the training data
# clf.fit(X_train, y_train)
#
# # Make predictions on the testing data
# predictions = clf.predict(X_test)
#
# # Evaluate the classifier
# accuracy = accuracy_score(y_test, predictions)
# print("Accuracy:", accuracy)
#
# # Get the classification report
# print(classification_report(y_test, predictions))
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import csv
x=[]
y=[]
yy=[]
target=[]
with open('train2.csv', mode ='r')as file:
# with open(r'C:\Users\lulub\PycharmProjects\proxy\dos\Wednesday-workingHours.pcap_ISCX.csv', mode ='r')as file:
# reading the CSV file
    csvFile = csv.reader(file)
    # displaying the contents of the CSV file
    i=0
    for lines in csvFile:
        if i!=0:
            try:
                r=[]
                # for ii in range(0,len(lines)-1):
                #     r.append(float(lines[0] ))
                r=[float(lines[0]),float(lines[1]),float(lines[2]),float(lines[3]),float(lines[4]),float(lines[5]),float(lines[6])]
                x.append(r)
                print(r)
                if lines[-1] not in yy:
                    yy.append(lines[-1])
                y.append(yy.index(lines[-1]))
            except:
                pass
        else:
            for ii in lines:
                target.append(ii)

        i=i+1
        print (i)
print(x)
print(y)

#
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_selection import SelectFromModel



# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.05, random_state=42)
X_test1=X_test
# Train decision tree classifier
# clf = DecisionTreeClassifier(random_state=42)
# clf.fit(X_train, y_train)
#
# # Feature selection using decision tree
# feature_selector = SelectFromModel(clf, prefit=True)
# X_train_selected = feature_selector.transform(X_train)
# X_test_selected = feature_selector.transform(X_test)
#
# # Print selected feature indices
# selected_feature_indices = feature_selector.get_support(indices=True)
# print("Selected feature indices:", selected_feature_indices)
# for i in selected_feature_indices:
#     print(target[i])
# # Get feature importances
# importances = clf.feature_importances_
#
# # Print feature importances
# print("Feature importances:")
# for i, importance in enumerate(importances):
#     print(f"Feature {i+1}: {importance}")
#
# # Select features with importance greater than a threshold
# threshold = 0.1
# selected_features = [i for i, importance in enumerate(importances) if importance > threshold]
#
# feature_selector = SelectFromModel(clf, threshold=0.1)
# selected_feature_indices = feature_selector.get_support(indices=True)
#
# # Generate a synthetic dataset
# # X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)
#
# # Split the dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Standardize features by removing the mean and scaling to unit variance
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# Initialize the MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=25)
neigh.fit(X_train, y_train)
# Predictions
y_pred_train = neigh.predict(X_train)
y_pred_test = neigh.predict(X_test)

# Calculate accuracy
train_accuracy = accuracy_score(y_train, y_pred_train)
test_accuracy = accuracy_score(y_test, y_pred_test)
print("KNN========================================")

print("Testing Accuracy:", test_accuracy)
#

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

y_pred_test = clf.predict(X_test)

# Calculate accuracy
train_accuracy = accuracy_score(y_train, y_pred_train)
test_accuracy = accuracy_score(y_test, y_pred_test)
print("DT========================================")

print("Testing Accuracy:", test_accuracy)

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf = clf.fit(X_train, y_train)

y_pred_test = clf.predict(X_test)

# Calculate accuracy
train_accuracy = accuracy_score(y_train, y_pred_train)
test_accuracy = accuracy_score(y_test, y_pred_test)
print("RF========================================")

print("Testing Accuracy:", train_accuracy)
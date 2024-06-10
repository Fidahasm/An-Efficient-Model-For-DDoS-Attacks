# from sklearn.neural_network import MLPClassifier
# from sklearn.datasets import make_classification
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import accuracy_score
# import csv
# x=[]
# y=[]
# yy=[]
# target=[]
# with open('Wednesday-workingHours.pcap_ISCX.csv', mode ='r')as file:
# # with open(r'C:\Users\lulub\PycharmProjects\proxy\dos\Wednesday-workingHours.pcap_ISCX.csv', mode ='r')as file:
# # reading the CSV file
#     csvFile = csv.reader(file)
#     # displaying the contents of the CSV file
#     i=0
#     for lines in csvFile:
#         if i!=0:
#             r=[]
#             # for ii in range(0,len(lines)-1):
#             #     r.append(float(lines[0] ))
#             r=[float(lines[0]),float(lines[1]),float(lines[2]),float(lines[3]),float(lines[4]),float(lines[5]),float(lines[6]),float(lines[7])]
#             x.append(r)
#             print(r)
#             if lines[-1] not in yy:
#                 yy.append(lines[-1])
#             y.append(yy.index(lines[-1]))
#         else:
#             for ii in lines:
#                 target.append(ii)
#
#         i=i+1
#         if i==50001:
#             break
#
# print(x)
# print(y)
#
#
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.feature_selection import SelectFromModel
#
#
#
# # Split data into train and test sets
# X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# X_test1=X_test
# # Train decision tree classifier
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
# # # Get feature importances
# # importances = clf.feature_importances_
# #
# # # Print feature importances
# # print("Feature importances:")
# # for i, importance in enumerate(importances):
# #     print(f"Feature {i+1}: {importance}")
# #
# # # Select features with importance greater than a threshold
# # threshold = 0.1
# # selected_features = [i for i, importance in enumerate(importances) if importance > threshold]
# #
# # feature_selector = SelectFromModel(clf, threshold=0.1)
# # selected_feature_indices = feature_selector.get_support(indices=True)
# #
# # # Generate a synthetic dataset
# # # X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)
# #
# # # Split the dataset into training and testing sets
# # X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
#
# # Standardize features by removing the mean and scaling to unit variance
# # scaler = StandardScaler()
# # X_train = scaler.fit_transform(X_train)
# # X_test = scaler.transform(X_test)
#
# # Initialize the MLPClassifier
# mlp = MLPClassifier(hidden_layer_sizes=(100, 50), activation='relu', solver='adam', max_iter=500, random_state=42)
#
# # Train the MLPClassifier
# mlp.fit(x, y)
#
# # Predictions
# y_pred_train = mlp.predict(X_test1)
# # y_pred_test = mlp.predict(x)
#
# # Calculate accuracy
# train_accuracy = accuracy_score(y_test, y_pred_train)
# # test_accuracy = accuracy_score(y, y_pred_test)
#
# print("Training Accuracy:", train_accuracy)
# # print("Testing Accuracy:", test_accuracy)
#

def predict_fn(r):
    try:
        l= mlp.predict([r])
        return l[0]
    except:
        if sum(r)>1:
            return 0
        else:
            return 1
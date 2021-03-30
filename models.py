import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.linear_model import Perceptron
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report

# Data preprocessing tools


def dataPreprocess(dataset, ratio):
    categorical = {'breast-cancer.csv': True,
                   'diabetes.csv': False,
                   'heart.csv': False,
                   'image.csv': True,
                   'waveform.csv': False,
                   'glass_csv.csv': True,
                   'segment_csv.csv': True}

    # Importing the dataset
    data = pd.read_csv(dataset)
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values

    # Encoding the Dependent Variable
    if(categorical[dataset.split('/')[-1]]):
        le = LabelEncoder()
        y = le.fit_transform(y)

    # Splitting the dataset into the Training set and Test set
    return train_test_split(X, y, test_size=ratio, random_state=1)


def driver(dataset, ratio):
    X_train, X_test, y_train, y_test = dataPreprocess(dataset, ratio)
    classificationReports = dict()

    model = Perceptron()
    model.fit(X_train, y_train)
    y_predP = model.predict(X_test)
    cr = classification_report(y_test, y_predP)

    print("Perceptron")
    print(cr)
    classificationReports["Perceptron"] = cr

    model = SVC()
    model.fit(X_train, y_train)
    y_predS = model.predict(X_test)
    cr = classification_report(y_test, y_predS)
    print("SVM")
    print(cr)
    classificationReports["Support Vector Classifier"] = cr

    model = GaussianNB()
    model.fit(X_train, y_train)
    y_predG = model.predict(X_test)
    cr = classification_report(y_test, y_predG)
    print("GaussianNB")
    print(cr)
    classificationReports["Gaussian Naive Bayes"] = cr

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    y_predD = model.predict(X_test)
    cr = classification_report(y_test, y_predD)
    print("Decision Tree")
    print(cr)
    classificationReports["Decision Tree"] = cr

    graClassifier = GradientBoostingClassifier()
    graClassifier.fit(X_train, y_train)
    y_pred = graClassifier.predict(X_test)
    cr = classification_report(y_test, y_pred)
    print("Gradient Boosting")
    print(cr)
    classificationReports["Gradient Boosting"] = cr

    return classificationReports


driver('https://raw.githubusercontent.com/bullet-ant/algorithmComparisionApp/main/Datasets/diabetes.csv', 0.2)

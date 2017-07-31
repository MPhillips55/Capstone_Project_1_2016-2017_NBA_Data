from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

# import dataset from data cleaning
df = pd.DataFrame.from_csv('merged_nba_data.csv')

# create won/loss column and remove from dataframe
y = df['win_or_loss']
df.drop('win_or_loss', axis=1, inplace=True)

# prepare data for machine learning
X = df.values

# use SSS to preserve ratio of classes
sss = StratifiedShuffleSplit(test_size=0.25)
sss.get_n_splits(X, y)

# split data into train/test sets
for train_index, test_index in sss.split(X, y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

# create classifier and parameter dict for gridsearch
clf = RandomForestClassifier(n_jobs=-1,random_state=20)

parameters = {'n_estimators':[15,20,30,32,40],
              'max_features':['auto', 'sqrt', 'log2'],
              'min_samples_split':[5,10,20,30,40]}

from sklearn.model_selection import GridSearchCV

# use gridsearch to find best parameters
CV_rfc = GridSearchCV(estimator=clf, param_grid=parameters, cv=sss)
CV_rfc.fit(X_train,y_train)

# create new classifier from best parameters
rfc = CV_rfc.best_estimator_

#predict from test set
pred = rfc.predict(X_test)

from sklearn.metrics import classification_report

# use class values to see how the model performed
print(classification_report(y_test, pred))
acc_score = (accuracy_score(y_test, pred) * 100)
print("The model predictes %.2f%% of the games it tests correctly.")

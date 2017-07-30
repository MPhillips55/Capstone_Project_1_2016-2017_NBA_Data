from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats


df = pd.DataFrame.from_csv('merged_nba_data.csv')

y = df['win_or_loss']

df.drop('win_or_loss', axis=1, inplace=True)

X = df.values

sss = StratifiedShuffleSplit(test_size=0.25)
sss.get_n_splits(X, y)

for train_index, test_index in sss.split(X, y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

clf = RandomForestClassifier(n_jobs=-1,random_state=20)

parameters = {'n_estimators':[15,20,30,32,40],
              'max_features':['auto', 'sqrt', 'log2'],
              'min_samples_split':[5,10,20,30,40]}

from sklearn.model_selection import GridSearchCV

CV_rfc = GridSearchCV(estimator=clf, param_grid=parameters, cv=sss)
CV_rfc.fit(X_train,y_train)

rfc = CV_rfc.best_estimator_

pred = rfc.predict(X_test)

from sklearn.metrics import classification_report

print(classification_report(y_test, pred))

fi = rfc.feature_importances_
fi_df = pd.DataFrame({'fi':fi})

fi_names = list(df.columns.values)
fi_names_df = pd.DataFrame({'fi_names':fi_names})

fi_imp = fi_names_df.join(fi_df)
fi_imp = fi_imp.sort_values(by='fi',ascending=False)
fi_imp.reset_index(drop=True,inplace=True)

ax = fi_imp.plot(kind='bar',figsize=(15,10))
ax.set_xticklabels(fi_imp.fi_names)



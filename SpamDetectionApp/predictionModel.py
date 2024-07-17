
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import joblib

mail_data=pd.read_csv('SpamDetectionApp/CSV_data/mail_data.csv')

mail_data.loc[mail_data['Category']=='spam','Category']=0

mail_data.loc[mail_data['Category']=='ham','Category']=1

X=mail_data['Message']
Y=mail_data["Category"]

x_train,x_test,y_train,y_test=train_test_split(X,Y, test_size=0.25, random_state=3)

vectorizer=TfidfVectorizer()
x_train_features=vectorizer.fit_transform(x_train)
x_test_feature=vectorizer.transform(x_test)

y_train=y_train.astype('int')
y_test=y_test.astype('int')

model=LogisticRegression()
model.fit(x_train_features,y_train)

joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(model, 'model.pkl')


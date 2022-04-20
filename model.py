import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier




df = pd.read_csv('Diabetes_Dataset.csv')
df = df[['Age', 'Blood_Glucose', 'Systolic_Blood_Pressure', 'Diastolic_Blood_Pressure', 'Insulin', 'BMI', 'Diabetes_Pedigree_Function', 'Diabetes']]
df['Diabetes'] = df['Diabetes'].astype('int')


x=df.iloc[:,:-1].values 
y=df.iloc[:,-1].values




# Model Building
from sklearn.model_selection import train_test_split
#spliting
X_train, X_test, y_train, y_test = train_test_split( x, y, test_size=0.25, random_state=4)


random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X_train, y_train)


# Creating a pickle file for the classifier
import pickle
filename = 'model.pkl'
pickle.dump(random_forest, open(filename, 'wb'))
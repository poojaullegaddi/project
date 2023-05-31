import pandas as pd

#kNN
from sklearn.neighbors import KNeighborsClassifier
#kNeighborsRegressor for regression
from sklearn.model_selection import train_test_split
import pickle
df=pd.read_csv('pizza.csv')
print(df.head())
x=df.iloc[:,:-1]
y=df.iloc[:,-1]
x_train, x_test,y_train, y_test = train_test_split(x,y,test_size=0.1)
modelp=KNeighborsClassifier(n_neighbors = 3)
modelp.fit(x_train,y_train)
p = modelp.predict([[25,69]])
print(p)
pickle.dump(modelp,open('pizza.pkl','wb'))

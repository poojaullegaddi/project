import pandas as pd
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pickle
df=pd.read_csv('diabetes.csv')
print(df.head())
x=df.iloc[:,:-1]
y=df.iloc[:,-1]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
modeld=KNeighborsClassifier(n_neighbors = 3)
modeld.fit(x_train,y_train)
p = modeld.predict([[4,110,92,0,0,37.6,0.191,30]])
print(p)
pickle.dump(modeld,open('diabetes.pkl','wb'))
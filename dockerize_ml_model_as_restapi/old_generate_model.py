from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier()
iris = datasets.load_iris()
X, y = iris.data, iris.target
model.fit(X, y)  



import pickle
pickle.dump(model, open('mymodel.pkl', 'wb'))
print('modelling done')

model2 = pickle.load(open('mymodel.pkl', 'rb'))
print('new model is loaded')

print(model2.predict(X[0:3]))

print(X[0:3])
print(type(X[0:3]))

print(y[0:3])
from sklearn import svm
from sklearn import datasets
from sklearn.externals import joblib

digits = datasets.load_digits()
clf = svm.SVC(gamma=0.001, kernel='rbf',cache_size=200)
clf.fit(digits.data[:-1], digits.target[:-1])
print(clf.predict(digits.data[-1:]))

clf.fit([[1],[2],[3],[4]],[1,2,3,4])
print(clf.predict([[2.6]]))

joblib.dump(clf,'filename.pkl')
clf2=joblib.load('filename.pkl')

print(clf2.predict([[2.6]]))


from sklearn import svm

X = [[12], [14], [16], [18], [20], [22], [24], [26]]
Y = [0, 0, 1, 0, 1, 0, 1, 1]

clf = svm.SVC(kernel='rbf').fit(X, Y)

print(clf.predict([[10], [15], [20], [25]]))

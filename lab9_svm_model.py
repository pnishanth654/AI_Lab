from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.svm import SVC

df = datasets.load_iris()
data = df.data
target = df.target

x = pd.Series(target).value_counts()
sns.barplot(x=x.index, y=x)
plt.show()

X = data
Y = target
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

svm = SVC(gamma='auto')
svm.fit(X_train, y_train)

yhat = svm.predict(X_test)
print("Accuracy Score = ", accuracy_score(y_test, yhat))
print(classification_report(y_test, yhat))

X_new = pd.DataFrame([[2, 2, 1, 0.2], [4.9, 2.2, 2.8, 1.1], [5.3, 2.5, 4.6, 1.9]])
prediction = svm.predict(X_new)
print("Prediction of Species:", prediction)
for i in prediction:
    print(df.target_names[i])
#call packages(Machine Learning decision tree)
from sklearn import tree 

#Data [Height, weight, shoe size]
x = [[170,70,9],[160,55,7],[160,55,7],[180,80,10],[180,80,10],[175,65,8],
         [175,65,8],[165,60,7.5],[165,60,7.5],[185,85,11],[185,85,11]]
y = ['male','female', 'female', 'male','female', 'male', 'female'
     'female', 'male','female','male','female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(x,y)     

predition = clf.predict([[150,60,9]])

print (predition)

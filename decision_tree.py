from sklearn import tree

#[height, weight, shoe size]
X= [[181,70,11],[165,65,7],[169,66,9],[166,70,10],[160,55,7],[180,70,10]]
Y= ['male','female','female','male','female','male']

clf=tree.DecisionTreeClassifier()     #classifier
clf=clf.fit(X,Y)
prediction= clf.predict([190,74,12])

print prediction

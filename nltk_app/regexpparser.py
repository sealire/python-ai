import nltk

a = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),
     ("the", "DT"), ("cat", "NN")]
b = [("The", "DT"), ("small", "JJ"), ("red", "JJ"), ("flower", "NN"),
     ("flew", "VBD"), ("through", "IN"), ("the", "DT"), ("window", "NN")]

grammer = 'NP:{<DT>*<JJ>*<NN>+}'
cp = nltk.RegexpParser(grammer)
tree = cp.parse(b)

print(tree)
tree.draw()

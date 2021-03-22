## Explaination on EQA:

Update:

**2020-02-28**

1.Discard rooms in the Z position  
2.Filter Z position objects based on their WordNet synset. Steps  
3.Remove “has*”  
4.Combine Original question and paths into a new question  


**2020-02-22**

For EQA, use the following：  
1.Object1 - R1 - Z - R2 - Object2  
2.E.g., cabinet - next to - microwave - located in - kitchen  
3.Optionally: keep one path for [object1, Z, object2]  
4.Two strategies  
&emsp;a) Path of length 2 only  
&emsp;b) N shortest paths

**2020-02-16**

1. you can find the dataset and my initial notebooks with some analysis here: https://drive.google.com/drive/u/1/folders/1TJ07cJk2q4dnyx9JrDr5xEYx6aI5mCSx  
    &emsp;a) the results of the notebook are obtained on a slightly different data - but I hope you can still use the notebook
2. download the dataset, ideally on a server
3. for each question of the training data, add a field called “cs” to the dictionary. The value of the key should be a list of edges that we find from CSKG. Let’s start with adding all triples, for all concepts in question (the dataset has a field that tells you which concept is the question about). You can use some of the code that gave us 3-4thousand edges for the 50 household concepts before.  
    &emsp;a) use the labels, so for example we would have [[“toaster”, “on top of”, “counter”], [“toaster”, “next to”, “coffee machine”]]
4. try to filter the noise from the “cs” triples. This could be done based on source (e.g., skip visual genome) and/or relation type (e.g., skip made-of) and/or node labels (e.g., skip triples where the object is not a household object and not a room).   
5. compute statistics: average number of triples per question, questions with no triples, distribution of number of triples over questions, etc.


# Class Creating practice


#Dog class test
import random

class Dog():
    
    def __init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age
    
    def bark(self):
        return 'woof'
    
    def fetch(self):
        n=random.randint(0,1)
        if n>=.5:
            return self.name +' found the ball'
        else:
            return self.name + ' could not find the ball...go get it yourself'
    
    
Fred=Dog('Fred', 'Chinese Shar Pei',4)
Fred.bark()
Fred.fetch()


#starting dataframe class text
class Corpus:
    
    def __init__(self, dataframe):
        self.dataframe=dataframe
        
    def column_length(self,column):
        return len(self.dataframe[column])
    
    def Custom_Tokenize(self,column):
        corpus=[]
        for i in range(self.dataframe[column]):
            text=self.dataframe[column][i]
            text=re.sub('[^a-zA-z]',' ',text)
            text=text.lower()
            text=text.split()
            text=' '.join(text)
            corpus.append(text)
            return corpus

import pandas as pd
import re 
data=pd.read_csv('data.csv',encoding='latin1')

data=Corpus(data)
data.column_length('Name')

data.Custom_Tokenize('Text')
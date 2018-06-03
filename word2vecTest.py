#word to vec test with gensim

#import libraries
from gensim.models import Word2Vec
import matplotlib.pyplot as plt

import plotly.offline as pyo
import plotly.plotly as py
import plotly.graph_objs as go

#create some sample sentences
sentences=[['i', 'am', 'experimenting', 'with', 'words', 'to' , 'vectors'],
           ['i','hope','this','will','yield','the','results','that','I','want'],
           ['this','will','be','applied','to','a','future','project'],
           ['it','is','related','to','the','regents','project','i','am','working','on','now'],
           ['hopefully','it','is','revealing'],
           ['this','will','improve','even','more']]

#set up word embeddings setting the min frequency quote and a 2 dimensional vector
model=Word2Vec(sentences,min_count=1,size=2)

#initiate vectors
word_vectors=model.wv

#get vector of a word
hope=word_vectors['hope']

#get x and y coordinates of chosen word
hope[0]
hope[1]

#assign vocabulary of model as an object
vocab=word_vectors.vocab

#get keys (words) of vector vocab dict
words=[word for word in vocab.keys()]

#get coordinates for words
x=[word_vectors[word][0] for word in words]
y=[word_vectors[word][1] for word in words]

#plot scatter plot with matplotlib
plt.scatter(x,y)
plt.title('Word2Vec Text Visual Representation')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

#plot scatter with plotly
trace=go.Scatter(x=x,
                 y=y,
                 mode='markers+text',
                 text=words,
                 textposition='top',
                 hoverinfo='none')

layout=go.Layout(title='Word2Vec Text Visual Representation',
                 xaxis=dict(title='X-axis',
                            zeroline=False),
                 yaxis=dict(title='Y-axis',
                            zeroline=False))

data=[trace]

fig=go.Figure(data=data,layout=layout)
pyo.iplot(fig)

#get similarity score -0.85867835313070628
model.wv.similarity('hope','results')
#word to vec test with gensim

#import libraries
from gensim.models import Word2Vec
import matplotlib.pyplot as plt

import plotly.offline as pyo
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
from sklearn.cluster import KMeans

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

'''
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
'''

#kmeans clustering
X=np.array([x,y])
X=X.transpose()

WCSS=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i, init='k-means++',max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    WCSS.append(kmeans.inertia_)
plt.plot(range(1,11),WCSS)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()


#Applying k-means to data
Num_Clusters=2
kmeans=KMeans(n_clusters=Num_Clusters, init='k-means++',max_iter=300, n_init=10, random_state=0)
y_kmeans=kmeans.fit_predict(X)

#Visualizing the Clusters
plt.scatter(X[y_kmeans==0,0],X[y_kmeans==0,1],s=100,c='red')
plt.scatter(X[y_kmeans==1,0],X[y_kmeans==1,1],s=100,c='blue')
'''
plt.scatter(X[y_kmeans==2,0],X[y_kmeans==2,1],s=100,c='green')
plt.scatter(X[y_kmeans==3,0],X[y_kmeans==3,1],s=100,c='cyan')
plt.scatter(X[y_kmeans==4,0],X[y_kmeans==4,1],s=100,c='magenta')
'''
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='yellow',label='Centroids')
plt.title('Word2vec Kmeans Clustering')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()

#get similarity score -0.85867835313070628
model.wv.similarity('hope','results')
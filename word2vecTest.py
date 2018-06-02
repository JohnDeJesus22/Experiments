#word to vec test with gensim

#import word2vec
from gensim.models import Word2Vec

#create some sample sentences
sentences=[['i', 'am', 'experimenting', 'with', 'words', 'to' , 'vectors'],
           ['i','hope','this','will','yield','the','results','that','I','want'],
           ['this','will','be','applied','to','a','future','project'],
           ['it','is','related','to','the','regents','project','i','am','working','on','now'],
           ['hopefully','it','is','revealing'],
           ['this','will','improve','even','more']]

#set up word embeddings setting the min frequency quote and a 2 dimensional vector
model=Word2Vec(sentences,min_count=1,size=2)

#get vector of a word
hope=model['hope']

#get x and y coordinates of those words
hope[0]
hope[1]

#assign vocabulary of model as an object
vocab=model.vocabulary

#failed since model.vocabulary isn't iterable
words=[word for word in vocab]

#get similarity score -0.85867835313070628
model.wv.similarity('hope','results')
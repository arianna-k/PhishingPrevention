# import required module
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import sys

# Function to find max element
# mat[][] : 2D array to find max element
def findMax(mat):
     
    # Initializing max element as INT_MIN
    maxElement = -sys.maxsize - 1
    element_index_x = 0
    element_index_y = 0
 
    # checking each element of matrix
    # if it is greater than maxElement,
    # update maxElement
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if (mat[i][j] > maxElement):
                maxElement = mat[i][j]
                element_index_x = i
                element_index_y = j
         
    # finally return maxElement
    return maxElement, element_index_x, element_index_y

# assign documents
d0 = 'A spectre is haunting Europe – the spectre of communism. All the powers of old Europe have entered into a holy alliance to exorcise this spectre: Pope and Tsar, Metternich and Guizot, French Radicals and German policespies'
d1 = 'Where is the party in opposition that has not been decried as communistic by its opponents in power? Where is the opposition that has not hurled back the branding reproach of communism, against the more advanced opposition parties, as well as against its reactionary adversaries? '
d2 = 'To this end, Communists of various nationalities have assembled in London and sketched the following manifesto, to be published in the English, French, German, Italian, Flemish and Danish languages'
 
# merge documents into a single corpus
string = [d0, d1, d2]
 
# create object
tfidf = TfidfVectorizer()
 
# get tf-df values
result = tfidf.fit_transform(string)
 
# get idf values
print('\nidf values:')
for ele1, ele2 in zip(tfidf.get_feature_names(), tfidf.idf_):
    print(ele1, ':', ele2)
 
# get indexing
print('\nWord indexes:')
print(tfidf.vocabulary_)
 
# display tf-idf values
print('\ntf-idf value:')
print(result)
 
# in matrix form
print('\ntf-idf values in matrix form:')
print(result.toarray())

print('\ntf-idf values after weighting:')

tf_idfArray = result.toarray()
for i in range(tf_idfArray[0].size):
    tf_idfArray[0][i] = tf_idfArray[0][i] * 3
for i in range(tf_idfArray[1].size):
    tf_idfArray[0][i] = tf_idfArray[0][i] * 2

print(tf_idfArray)
for i in range(5):
    maxElement, element_index_x, element_index_y = findMax(tf_idfArray)
    print(findMax(tf_idfArray))
    word = list(tfidf.vocabulary_.keys())[list(tfidf.vocabulary_.values()).index(element_index_y)]
    print(word)
    tf_idfArray[element_index_x][element_index_y] = 0.0

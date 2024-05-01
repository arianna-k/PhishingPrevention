# import required module
from sklearn.feature_extraction.text import TfidfVectorizer
import sys
from serpapi import GoogleSearch
import requests
from bs4 import BeautifulSoup

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

def unknownLinkChecker(url):
    # making requests instance
    reqs = requests.get(url)
    
    # using the BeautifulSoup module
    soup = BeautifulSoup(reqs.text, 'html.parser')

    # assign documents
    # Find the title
    for title in soup.find_all('title'):
        print(title.get_text())
        d0 = title.get_text()
    #Extract the metadata
    d1 = soup.find_all('meta')
    d1= str(d1)
    #Extract the body text 
    d2 = soup.get_text()
    #print(d2)
    
    # merge documents into a single corpus
    string = [d0, d1, d2]
    
    # create object
    tfidf = TfidfVectorizer()
    
    # get tf-df values
    result = tfidf.fit_transform(string)
    
    # get idf values
    # print('\nidf values:')
    # for ele1, ele2 in zip(tfidf.get_feature_names(), tfidf.idf_):
    #     print(ele1, ':', ele2)
    
    # # get indexing
    # print('\nWord indexes:')
    # print(tfidf.vocabulary_)
    
    # # display tf-idf values
    # print('\ntf-idf value:')
    # print(result)
    
    # # in matrix form
    # print('\ntf-idf values in matrix form:')
    # print(result.toarray())

    print('\ntf-idf values after weighting:')

    tf_idfArray = result.toarray()
    for i in range(tf_idfArray[0].size):
        tf_idfArray[0][i] = tf_idfArray[0][i] * 3
    for i in range(tf_idfArray[1].size):
        tf_idfArray[0][i] = tf_idfArray[0][i] * 2

    print(tf_idfArray)
    query_search = ''
    counter = 0
    while counter < 7:
        maxElement, element_index_x, element_index_y = findMax(tf_idfArray)
        print(findMax(tf_idfArray))
        word = list(tfidf.vocabulary_.keys())[list(tfidf.vocabulary_.values()).index(element_index_y)]
        if word != ('for' or 'and' or 'of' or 'the' or 'is'):
            query_search += word
            query_search += ' '
            counter += 1
        tf_idfArray[element_index_x][element_index_y] = 0.0
    
    print(query_search)
    
    search = GoogleSearch({
        "q": query_search, 
        "location": "Richmond,Virginia",
        "api_key": "7b7162d3bb3850756a751d4a66c57d0c8db9129aff7f4e503a4b7dd07bcd9378",
        "num" : 50
    })
    result = search.get_dict()

    link_found = False
    print(result['organic_results'])

    for item in result['organic_results']:
        link = item['link']
        if link == url:
            print('found link')
            link_found = True
            break
        link = item['displayed_link']
        if link == url:
            print('found link')
            link_found = True
            break

    return(link_found)

#driver code
if __name__ == "__main__":
 
    # target url
    url = 'https://www.geeksforgeeks.org/'


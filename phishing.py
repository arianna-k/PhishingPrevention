from sklearn.feature_extraction.text import TfidfVectorizer
import sys
#from serpapi import GoogleSearch
import requests
#from bs4 import BeautifulSoup
import string
import re
from urllib.parse import urlparse

class Email:
    def __init__(self, sender, subject, body):
        self.sender = sender
        self.subject = subject
        self.body = body
        self.attachments = []

    def add_attachment(self, attachment):
        self.attachments.append(attachment)

def extract_domain(url):
    if isinstance(url, bytes):
        url = url.decode('utf-8')  # Convert bytes to string using UTF-8 encoding
    parsed_url = urlparse(url)
    if parsed_url.netloc:
        return parsed_url.netloc
    else:
        # For URLs without a scheme (e.g., "www.example.com")
        return parsed_url.path.split('/')[0]


def extract_links(text):
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    links = re.findall(url_pattern, text)
    print(links)
    return links
    
def strip_punctuation(text):
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    translation_table = str.maketrans("", "", punctuation_chars)
    return text.translate(translation_table)

def check_typos(string, dictionary):
    words = strip_punctuation(string).split()  # Split the string into words
    num_typos = sum(1 for word in words if word.lower() not in dictionary)
    for word in words:
        if word.lower() not in dictionary:
            num_typos += 1
    return num_typos

def check_contents(string):
    words = strip_punctuation(string)
    suspicious = {"congratulations", "urgent", "request", "now", "fail", "failed", "payment", "purchase", "required", "action"}
    return any(word.lower() in suspicious for word in string.split())

def check_attachment(attachment):
    phishing_file = "ALL-phishing-domains.txt"
    try:
        with open(phishing_file, 'r') as file:
            phishing_URLS = set(line.strip() for line in file)
    except FileNotFoundError:
        print(f"Error: Unable to open file {phishing_file}")
        return
        
    if attachment in phishing_URLS:
        return True
    return False


def check_domains(attachments):
    phishing_file = "ALL-phishing-domains.txt"
    try:
        with open(phishing_file, 'r') as file:
            phishing_URLS = set(line.strip() for line in file)
            print(phishing_URLS)
    except FileNotFoundError:
        print(f"Error: Unable to open file {phishing_file}")
        return
    
    for attachment_list in attachments:
        for attachment in attachment_list:
            # Split the URL into parts based on the URL structure
            parts = attachment.split("//")[-1].split("/")
            if len(parts) >= 2:
                # Extract domain and subdomains
                domain_parts = parts[0].split(".")
                
                # Extract top-level domain (TLD) and second-level domain (SLD)
                tld = domain_parts[-1]  # Last part is the TLD
                sld = domain_parts[-2] if len(domain_parts) > 1 else ""  # Second-to-last part is the SLD, if available

                # Print extracted TLD and SLD for debugging
                # print("TLD:", tld)
                # print("SLD:", sld)
                
                # Check if the TLD or SLD is in the phishing URLs set
                if tld in phishing_URLS or sld in phishing_URLS:
                    return True
    return False

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

    

def main():
    dictionary_file = "dictionary.txt"
    try:
        with open(dictionary_file, 'r') as file:
            dictionary = set(line.strip() for line in file)
    except FileNotFoundError:
        print(f"Error: Unable to open file {dictionary_file}")
        return

    if len(sys.argv) == 1:
        # No input file provided, so get email details from user input
        sender = input("Enter the sender: ")
        subject = input("Enter the subject: ")
        body = input("Enter the body: ")
        attachments = []
        print("Enter the attachments/links (Enter one at a time, type 'Done' when finished)")
        while True:
            attachment = input()
            if attachment.lower() == "done":
                break
            else:
                attachments.append(attachment)
        email = Email(sender, subject, body)
        email.attachments = attachments
        email.attachments.append(extract_links(email.body))

    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        try:
            with open(filename, 'r') as inputFile:
                sender = inputFile.readline().strip()
                subject = inputFile.readline().strip()
                body = inputFile.read()
                attachments = []  # Placeholder for attachments found in the body
        except FileNotFoundError:
            print(f"Error: Unable to open file {filename}")
            return

        email = Email(sender, subject, body)
        email.attachments = extract_links(email.body)

    else:
        print("Usage: One file at a time!")
        return

    score = 0
    # Check for Typos
    typos= check_typos(email.body, dictionary)
    if typos > 20:
        score += 10
    elif typos > 10:
        score += 5
    elif typos > 5:
        score += 2

    # Check for suspicious words
    if check_contents(email.subject):
        score += 10
    
    if check_contents(email.body):
        score += 5

    url = "https://www.example.com/path/to/page"
    domain = extract_domain(url)
    print(domain)  # Output: www.example.com

    #If a link is not found in the database, run it through the link_checker
    for attachment in email.attachments:
        domain = extract_domain(attachment)
        if check_attachment(domain):
            score = 99
        elif unknownLinkChecker(attachment):
            score += 12
        else:
            score += 88

    if score > 99:
        score = 99
    
    print(f"This email is {score}% likely to be a phishing scam!")


if __name__ == "__main__":
    main()

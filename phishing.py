import sys
import string
import re

class Email:
    def __init__(self, sender, subject, body):
        self.sender = sender
        self.subject = subject
        self.body = body
        self.attachments = []

    def add_attachment(self, attachment):
        self.attachments.append(attachment)

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

def check_attachments(attachments):
    phishing_file = "ALL-phishing-domains.txt"
    try:
        with open(phishing_file, 'r') as file:
            phishing_URLS = set(line.strip() for line in file)
    except FileNotFoundError:
        print(f"Error: Unable to open file {phishing_file}")
        return
    
    for attachment_list in attachments:
        for attachment in attachment_list:
            domain = attachment.split("//")[-1].split("/")
            if len(domains) >= 2:
                domain = domains[0]
                print(domain)
                if domain in phishing_URLS:
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

    # Check all attachments for suspicious links
    print(attachments)
    phishingURL = check_attachments(email.attachments)
    if phishingURL == True:
        score = 99

    print(f"This email is {score}% likely to be a phishing scam!")


if __name__ == "__main__":
    main()

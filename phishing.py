import sys

class Email:
    def __init__(self, sender, subject, body):
        self.sender = sender
        self.subject = subject
        self.body = body
        self.attachments = []

    def add_attachment(self, attachment):
        self.attachments.append(attachment)

def strip_punctuation(text):
    punctuation_chars = "!#$%&'()*+,-./:;<=>?@`{|}"
    return ''.join(char for char in text if char not in punctuation_chars)

def check_typos(string, dictionary):
    words = string.split()
    words = strip_punctuation(words)
    num_typos = sum(1 for word in words if word.lower() not in dictionary)
    return num_typos

def check_contents(string):
    words = string.split()
    words = strip_punctuation(words)
    suspicious = {"congratulations", "urgent", "must", "now", "fail", "failed", "payment", "purchase", "required", "action"}
    return any(word.lower() in suspicious for word in string.split())

def check_attachments(attachments):
    # Implement this function to check attachments for suspicious links
    pass

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
        email.attachments = attachments

    else:
        print("Usage: One file at a time!")
        return

    score = 0
    # Check for Typos
    typos= check_typos(email.body, dictionary)
    print(typos)
    if typos > 20:
        score += 15
    elif typos > 10:
        score += 10
    elif typos > 5:
        score += 5
    elif typos > 1:
        score += 2

    # Check for suspicious words
    if check_contents(email.subject):
        score += 10

    # Check all attachments for suspicious links
    check_attachments(email.attachments)

    print(f"This email is {score}% likely to be a phishing scam!")

if __name__ == "__main__":
    main()

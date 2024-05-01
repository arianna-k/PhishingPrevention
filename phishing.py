import sys

class Email:
    def __init__(self, sender, subject, body):
        self.sender = sender
        self.subject = subject
        self.body = body
        self.attachments = []

    def add_attachment(self, attachment):
        self.attachments.append(attachment)

def checktypos(string):
    words = string.split()
    # Iterate over each word
    number = 0
    for word in words:
        #Finish with asc or a private dictionary
        if word in dictionary:
            number += 1
    return number

def checkcontents(string):
    suspicious = ["congratulations", "urgent", "must", "now", "fail", "failed", "payment", "purchase", "required"]
    words = string.split()
    # Iterate over each word
    for word in words:
        if word in suspicious:
            return True

def main():
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
                # Add function to search through body and find attachments
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
    typos = checktypos(email.body)
    if typos > 20:
        typoScore = 15
    elif typos > 10:
        typoScore = 10
    elif typos > 1:
        typoScore = 5
    score += typoScore
    
    # Check for suspicious words
    if checkcontents(email.subject) = True:
        score += 10
    #Check all attachments for suspicious links

    print(f"This email is {score}% likely to be a phishing scam!")

if __name__ == "__main__":
    main()

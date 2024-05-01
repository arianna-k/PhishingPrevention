#include "Email.h"
#include <iostream>
#include <sstream>
#include <cctype>
#include <fstream>


using namespace std;

int numberTypos(Email email){
    string body = email.body;
    /*Check the body for content that could be suspicious. EX)
    Too good to be true email: Giving you free stuff
    Urgency: you must change your password at this link
    */
    istringstream iss(body);
    //Check each word to see if there are typos 
    while(iss){
        
    }
}

bool hasSuspiciousContent(Email email){
    string body = email.body;
    /*Check the body for content that could be suspicious. EX)
    Too good to be true email: Giving you free stuff
    Urgency: you must change your password at this link
    */
    istringstream iss(body);
    string Word;
    //Check each word to see if it is a suspicious word 
    while(iss >> Word){
        string word = tolower(word);
        if(word == "congratulations" || word == "urgent")
    }
}

bool hasSuspiciousAttachments(Email email){
    vector<string> attachments = email.attachments;

}

int percentagePhishing(Email email){
    int score = 0;
    if(hasSuspiciousContent(email) == true){
        score += 5;
    }
    if(hasSuspiciousAttachments(email) == true){
        score += 20;
    }
}

int main(int argc, char *argv[]){
    if (argc == 0){
        //No input so have user copy and paste email into terminal
        string sender;
        cout << "Enter the sender:";
        cin >> sender;
        string subject;
        cout << "Enter the subject:";
        cin >> subject;
        string body;
        cout << "Enter the body";
        cin >> body;
        vector<string> attachments;
        string input;
        Email email = Email(sender, subject, body);
        cout << "Enter the attachments/ links (Enter one as a time, type Done when there are no more)";
        while (true){
            cin >> input;
            if(input == "done" || input == "Done" || input == "DONE"){
                break;
            }
            else{
                email.addAttachment(input);
            }
        }
    }
    else if (argc == 1){
        string filename = argv[1];
        ifstream inputFile(filename);
        if (!inputFile) {
            std::cerr << "Error: Unable to open file " << filename << std::endl;
            return 1;
        }
        string sender;
        getline(inputFile, sender);
        string subject;
        getline(inputFile, subject);
        string body;
        string line;
        while(getline(inputFile, line)){
            body += line;
        }
        //Add function to search through body and find attachments
        
    }
    else{
        std::cerr << "Usage: One file at a time!" << std::endl;
        return 1;
    }
    //Go through the emails and return a score
    int score;
    cout << "This email is " << score << "% likely to be a phishing scam!";
    return 0;
}
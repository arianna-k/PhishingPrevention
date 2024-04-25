#include "Email.h"
#include <iostream>
#include <sstream>

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
    //Check each word to see if it is a suspicious word 
    while(iss){
        
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
        cout << "Enter the attachments/ links (Enter one as a time, type Done when there are no more)";
        while (true){
            cin >> input;
            if(input == "done" || input == "Done" || input == "DONE"){
                
            }
        }
    }
    else{
        
        
    }
    //Go through the emails and return a score
    int score;
    cout << "This email is " << score << "% likely to be a phishing scam!";
    return 0;
}
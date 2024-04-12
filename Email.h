#ifndef EMAIL_H
#define EMAIL_H

#include <string>
#include <vector>

using namespace std;

struct Email {
    //Variable Fields
    string sender;
    string subject;
    string body;
    vector<string> attachments;

    //Constructors
    Email(string sender, string subject, string body, vector<string> attachments);
    Email(string email);

    //Function Methods
    void addAttachment(string);
};

#endif
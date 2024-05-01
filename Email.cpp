#include "Email.h"

using namespace std;

Email::Email(string sender, string subject, string body)
    : sender(sender), subject(subject), body(body) {}

void Email::addAttachment(string input){
    attachments.push_back(input);
}
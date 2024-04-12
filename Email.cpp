#include "Email.h"

using namespace std;

Email:: Email(string sender, string subject, string body, vector<string> attachments)
    : sender(sender), subject(subject), body(body), attachments(attachments) {}

Email:: Email(string email) {}

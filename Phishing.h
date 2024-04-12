#ifndef PHISHING_H
#define PHISHING_H

#include "Email.h"
#include <string>
#include <vector>

class Phishing{
    public:
        bool hasSuspiciousContent(Email email);
        bool hasSuspiciousAttachments(Email email);

    private:    
        int numberTypos(Email email);
};

#endif
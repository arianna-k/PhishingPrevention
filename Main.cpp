#include "Email.h"
#include "Phishing.h"
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char *argv[]){
    if (argc == 0){
        //No input so have user copy and paste email into terminal

    }
    else{
        //Go through each text file and make it an email!
        for (int i = 1; i < argc; i++){
            std::ifstream infile(argv[i]); //  open the input file for reading
            if (!infile) { // if file can't be opened, need to let the user know
                std::cerr << "Error: could not open file: " << argv[i] << std::endl;
                exit(1);
        }
        }
    }
}
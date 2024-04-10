// 2.1 Notes (The Parts of a C++ Program)

#include <iostream> //preprocessor directive

using namespace std;   //namespace to use (not familiar with term, worry about later)
int main()        //declaring my function
{
    cout << "Hello world!";

    // std:string cout_applied = coutPractice();
    // std::cout << cout_applied << std::endl;

    return 0;
}

/*
    // -- Begins a comment (though just one line)
    # --  Begins preprocessor directive
    <> -- Encloses filename used in directive
    () -- Used when naming a function
    {} -- Encloses a group of statements
    "" -- Encloses a string of characters
    ;  -- Ends a programming statement
*/

// cout object

std::string coutPractice ()
{
    string greeting1 = "Hello, world!!";
    string greeting2 = "Vs. using two <<, << to make this!";
    string greeting_w_slash_n = "And the good ol\nslash n to make a new line";

    string combinedGreeting = greeting1 + greeting2 + greeting_w_slash_n;

    return combinedGreeting;
}

int variablePractice()
{
    int age = 12;
    return age;
}


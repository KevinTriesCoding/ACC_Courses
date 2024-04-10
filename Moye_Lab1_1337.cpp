#include <iostream>

int main() {
// variable raw_he
    int raw_height;
    std::cout << "What is the basketball player's height (inches): ";
    std::cin >> raw_height;

    int feet_height = raw_height/ 12;
    int inch_height = raw_height % 12;

    std::cout << raw_height;
    std::cout << feet_height;
    std::cout << inch_height;

}


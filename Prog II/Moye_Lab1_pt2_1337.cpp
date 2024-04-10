#include <iostream>

int main() {
    
    int bball_height = 74;
    int height_ft = bball_height / 12;
    int height_in = bball_height % 12;

    std::cout << "A " << bball_height << " inch tall basketball player is " << height_ft << " ft " << height_in << " in tall.\n";
    

}

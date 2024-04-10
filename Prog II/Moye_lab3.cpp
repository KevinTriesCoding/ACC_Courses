#include <iostream>
using namespace std;

void getSales(string region, int& sales); //int& to allow getSales to change values stored in arrays
void findHighest (int salesArray[], string regionArray[], int size);

int main() {
    //Set up arrays to store values for division sales and the division for display
    string regionArray[4] = {"Northeast Division", "Southeast Division", "Northwest Division", "Southwest Division"};
    int NE_Sales, SE_Sales, NW_sales, SW_sales;
    int salesArray[4] = {NE_Sales, SE_Sales, NW_sales, SW_sales};
    
    // loop through all 4 indexes of both arrays
    // pass both the arrays to getSales; regionArray cycles through array to get printed; salesArray gets assigned user input values 
    // (where int& is utilized)
    for (int i = 0; i < 4; i++) {
        getSales(regionArray[i], salesArray[i]);
    }

//pass both arrays through findHighest and set the size to array size of 4
findHighest(salesArray, regionArray, 4);

}

void getSales(string region, int& sales) {
//collects user inputs for the 4 regions
//will store the values into regionArray and salesArray 

    cout << "Enter the quarterly sales for the " << region << ": ";
    cin >> sales;

    while (sales <= 0) {
        cout << "Sales figure cannot be negative or 0. Please re-enter: ";
        cin >> sales;
    }

    } 

void findHighest (int salesArray[], string regionArray[], int size) {
//loops through the arrays to find highest sales value and region associated with it
    int highNum = 0; // keep track of highest sale
    int highRegion = 0; // index tracking for region
    for (int i = 0; i < 4; i++) {
        if (salesArray[i] > highNum) {
            highNum = salesArray[i];
            highRegion = i;
        } 
    }
    cout << "The " << regionArray[highRegion] << "had the highest sales this quarter." << endl;
    cout << "Their sales were $" << highNum << "!"; 

}
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    // Variables for quantity, total, and discounts to set up logic tree
    int amount_purchased;
    cout << "How many software units are being purchased: ";
    cin >> amount_purchased;

    const int discount_20 = 19;
    const int discount_30 = 49;
    const int discount_40 = 99;
    const int discount_50 = 100;

    double total_price = 199 * amount_purchased;
    double discounted_total = total_price;

    // Logic tree for discounts based on amount purchased
    if (amount_purchased >= 10 && amount_purchased <= discount_20) {
        discounted_total = total_price - (total_price * 0.20);
    }
    else if (amount_purchased > discount_20 && amount_purchased <= discount_30) {
        discounted_total = total_price - (total_price * 0.30);
    }
    else if (amount_purchased > discount_30 && amount_purchased <= discount_40) {
        discounted_total = total_price - (total_price * 0.40);
    }
    else if (amount_purchased >= discount_50) {
        discounted_total = total_price - (total_price * 0.50);
    }

    // Print statement to display total after discount applied
    cout << "The total cost of the purchase is $" << fixed <<  setprecision(2) << discounted_total << endl;

    return 0;
}

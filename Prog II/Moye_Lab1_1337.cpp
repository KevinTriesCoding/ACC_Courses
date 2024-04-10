
# include <iostream>


int main(){
    // Variables for static employee income and user_selet declared for input statement
    int employee_income = 39000;
    int user_select;

    
    std::cout << "How frequently do you get paid (1 for bi-weekly, 2 for bi-monthly): "; 
    std::cin>> user_select;

    float bi_weekly_pay = employee_income/26;
    float bi_monthly_pay = employee_income/24;

    std::cout << "Gross pay per bi-monthly paycheck: $" << bi_weekly_pay << "\n";
    std::cout << "Gross pay per bi-weekly paycheck: $" << bi_monthly_pay << "\n";

    // Not necessary for assignment, just for practice w/ if statements and inputs
    if (user_select == 1) {
        std::cout << "\nYou selected 1. Your gross pay per bi-monthly paycheck: $" << bi_weekly_pay << "\n";
    }
    else if (user_select == 2) {
            std::cout << "\nYou selected 2. Your gross pay per bi-weekly paycheck: $" << bi_monthly_pay << "\n";
    }

    else {
        std::cout << "\nError - User did not choose 1 or 2";
    }


}

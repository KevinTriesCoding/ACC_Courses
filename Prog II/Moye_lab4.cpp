#include <iostream>
using namespace std;

class Population {
    private:
        int total_pop, annual_birth, annual_death;

    public:
    // constructor
    Population() : total_pop(2), annual_birth(0), annual_death(0) {}
    Population (int pop, int birth, int death) {
        setPopulation (pop);
        setAnnualBirth (birth);
        setAnnualDeath (death);
    }

    //setter functions
    void setPopulation (int pop) {
        if (pop < 2) {
            total_pop = 2;
        } else {
            total_pop = pop;
        }
    }
    void setAnnualBirth(int birth) {
        if (birth < 0) {
            annual_birth = 0;
        } else {
            annual_birth = birth;
        }
    }
    void setAnnualDeath(int death) {
        if (death < 0) {
            annual_death = 0;
        } else {
            annual_death = death;
        }
    }

    //getter functions
    double getBirthrate () {
        double birth_rate = (annual_birth * 1.0) / total_pop;
        return birth_rate;

    }

    double getDeathrate () {
        double death_rate = (annual_death * 1.0) / total_pop;
        return death_rate;
    }

}; 

int main () {

    int total_pop, annual_birth, annual_death;
    cout << "Enter total population: ";
    cin >> total_pop;

    cout << "Enter annual number of births: ";
    cin >> annual_birth;

    cout << "Enter annual number of deaths: ";
    cin >> annual_death;

    Population population (total_pop, annual_birth, annual_death);

    cout << "Birth Rate: " << population.getBirthrate() << endl;
    cout <<  "Death Rate: " << population.getDeathrate() << endl;


    Population errorPop(-5, -10, -3);
    cout << "Birth Rate (invalid data): " << errorPop.getBirthrate() << endl;
    cout << "Death Rate (invalid data): " << errorPop.getDeathrate() << endl;


}
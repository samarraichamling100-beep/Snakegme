#include <iostream>
#include <random>

int main() {

    int rand_num;
    int PlayerGuess;
    int attempts = 0;

    std::random_device rd;
    std::mt19937 gen(rd());

    std::uniform_int_distribution<> Rand_Num(1, 100);

    rand_num = Rand_Num(gen);

    std::cout << "Guess a number from 1-100\n";

    while (true) {

        std::cin >> PlayerGuess;
        attempts++;

        if (PlayerGuess > rand_num) {
            std::cout << "Too high!\n";
        }
        else if (PlayerGuess < rand_num) {
            std::cout << "Too low!\n";
        }
        else {
            std::cout << "Correct! The number was "
                      << rand_num << "\n";

            std::cout << "Attempts: "
                      << attempts << "\n";

            break;
        }
    }

    return 0;
}
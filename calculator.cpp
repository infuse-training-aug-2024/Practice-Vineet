#include <iostream>

using namespace std;

class Calculator {
public:
    // Method to perform addition
    double add(double a, double b) {
        return a + b;
    }
    
    // Method to perform subtraction
    double subtract(double a, double b) {
        return a - b;
    }

    double subtract2(double a, double b, double c){
        return a-b-c;
    }
    
    // Method to perform multiplication
    double multiply(double a, double b) {
        return a * b;
    }
    
    // Method to perform division
    double divide(double a, double b) {
        if (b != 0)
            return a / b;
        else {
            cout << "Error! Division by zero." << endl;
            return 0;
        }
    }
};

int main() {
    Calculator calc;
    double num1, num2;
    char operation;
    
    cout << "Enter first number: ";
    cin >> num1;
    
    cout << "Enter an operator (+, -, *, /): ";
    cin >> operation;
    
    cout << "Enter second number: ";
    cin >> num2;
    
    double result;
    switch(operation) {
        case '+':
            result = calc.add(num1, num2);
            break;
        case '-':
            result = calc.subtract(num1, num2);
            break;
        case '*':
            result = calc.multiply(num1, num2);
            break;
        case '/':
            result = calc.divide(num1, num2);
            break;
        default:
            cout << "Error! Operator is not correct" << endl;
            return 1;
    }
    
    cout << "Result: " << result << endl;
    
    return 0;
}

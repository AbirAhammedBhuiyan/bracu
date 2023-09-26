#include <stdio.h>
#include <stdlib.h>

float add(float x, float y) {
    return x+y;
}

float sub(float x, float y) {
    return x-y;
}

float mul(float x, float y) {
    return x*y;
}

int main() {

    float x, y;
    char operator;

    printf("Enter first number: ");
    scanf("%f", &x);

    printf("Enter second number: ");
    scanf("%f", &y);

    printf("Enter the operator: ");
    scanf(" %c", &operator);

    if (x > y)
        printf("Result: %f\n", sub(x, y));
    if (x < y) 
        printf("Result: %f\n", add(x, y));
    if (x == y)
        printf("Result: %f\n", mul(x, y));

   return 0; 

}

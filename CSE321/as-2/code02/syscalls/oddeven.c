#include <stdio.h>
#include <stdlib.h>


int oddEven(int num) {
    if (num%2 == 0)
        return 0;
    return 1;
}


int main(int argc, char *argv[]) {

    int num;

    if (argc < 2) {
        printf("No number provided\n");
        return -1;
    }

    for (int i=1; i<argc; i++) {
        num = atoi(argv[i]);
        printf("%d -> %s\n", num, oddEven(num) ? "Odd" : "Even");
    }

    return 0;
}

#include <stdio.h>
#include <stdlib.h>

int isPerfect(int num) {
    int sum = 0;
    for(int i=1; i<num; i++) {
        if (num%i == 0) {
            sum += i;
        }
    }

    if (sum > 0 && num == sum) 
        return 1;

    return 0;
}

void perfectPrinter(int start, int end) {
    if (start && end) {
        for (int i=start; i<=end; i++) {
            if (isPerfect(i))
                printf("%d\n", i);
        }
    } else {
        printf("Error\n");
    }
}


int main() {

    int start = 0;
    int end = 0;

    scanf("%d", &start);
    scanf("%d", &end);

    perfectPrinter(start, end);

    return 0;
}

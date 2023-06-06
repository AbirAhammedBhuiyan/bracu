#include <stdio.h>
#include <stdlib.h>

int compareInt(const void *a, const void *b) {
    return *(int*)b - *(int*)a;
}

void printArray(int *arr, int size) {
    for (int i=0; i<size; i++) {
        printf("%d ", arr[i]);
    }

    printf("\n");
}


int main(int argc, char *argv[]) {

    int size = argc - 1;
    int arr[size];

    if (argc < 2) {
        printf("No number provided\n");
        return -1;
    }

    for (int i=0; i<size; i++) {
        arr[i] = atoi(argv[i+1]);
    }

    printf("Before sort\n");
    printArray(arr, size);

    qsort(arr, size, sizeof(arr[0]), compareInt);

    printf("After sort\n");
    printArray(arr, size);

    return 0;

}

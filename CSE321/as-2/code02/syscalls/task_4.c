#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

// making argument from argv that can be passed to execv
char **argMaker(int *arr, int size, char *progName) {

    char **args = malloc(sizeof(char*) * (size+2));

    args[0] = progName;

    for(int i=0; i<size; i++) {
        char *buffer = malloc(10);
        sprintf(buffer, "%d", arr[i]);
        args[i+1] = buffer;
    }

    args[size+1] = NULL;

    return args;
}


int main() {

    int array[] = {22, 11, 9, 5, 23};
    int size = sizeof(array)/sizeof(array[0]);

    if (fork() == 0) {

        printf("Running Child Process:\n");
        char **args = argMaker(array, size, "./sort");
        if (execv("./sort", args) == -1) {
            printf("`sort` binary not found\n");
            free(args);
            return -1;
        }

        free(args);

        return 0;

    } else {

        wait(NULL);
        char **args = argMaker(array, size, "./oddeven");
        printf("Running Parent Process:\n");
        if (execv("./oddeven", args) == -1) {
            printf("`oddeven` binary not found\n");
            free(args);
            return -1;
        }

        free(args);

        return 0;

    }

}

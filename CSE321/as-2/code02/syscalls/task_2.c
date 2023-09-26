#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>


int main() {


    if (fork() == 0) {

        printf("I am child\n");

        if (fork() == 0) {

            printf("I am grandchild\n");
            return 0;

        }

        return 0;

    } else {

        printf("I am parent\n");
        return 0;

    }

}

#include <stdio.h>
#include <unistd.h>

#define LEN 3

int main() {

    int fd[2];
    pipe(fd);           // defining pipe for interprocess communication

    if (fork() == 0) {
        int y;
        read(fd[0], &y, sizeof(int));
        printf("%d. Child process ID: %d\n", ++y, getpid());
        write(fd[1], &y, sizeof(int));
        close(fd[0]);
        close(fd[1]);

        for (int i=0; i<LEN; i++) {
            ++y;
            if (fork() == 0) {
                printf("%d. Grandchild process ID: %d\n", y, getpid());
                return 0;
            }
        }

        return 0;

    } else {
        int x = 0;
        close(fd[0]);
        printf("%d. Parent process ID: %d\n", ++x, getpid());
        write(fd[1], &x, sizeof(int));
        close(fd[1]);

        return 0;

    }

}


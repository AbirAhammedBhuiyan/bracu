#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <errno.h>


int main() {

    pid_t a, b, c;
    int x = 0;
    int fd[2];
    pipe(fd);               // defining pipe for interprocess communication

    a = fork();
    b = fork();
    c = fork();
    
    if (a>0 && b>0 && c>0) {

        // waiting for all the child process to finish their execution
        while (wait(NULL) != -1 || errno != ECHILD);

        close(fd[1]);
        
        int i=1; 

        while (read(fd[0], &x, sizeof(int)) != 0) {
            i++;
        }
        printf("Total processes: %d\n", i);
        close(fd[0]);
    } else {

        printf("In child %d\n", getpid());
        write(fd[1], &x, sizeof(int));
        pid_t gc = -1;

        if (getpid() % 2) {
            gc = fork();
            if (gc == 0) {
                write(fd[1], &x, sizeof(int));
                printf("Inside fork %d my parent %d\n", getpid(), getppid()); 
                return 0;
            }
        }

        // waiting for grand child process to finish its execution
        if (gc != -1) {
            waitpid(gc, NULL, 0);
        }

        return 0;
    }

    return 0;

}
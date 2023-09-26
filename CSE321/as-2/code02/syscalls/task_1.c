#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>

#define MAX 100


int main(int argc, char *argv[]) {

    int n, fd;
    char buffer[MAX];
    char newLine[] = "\n";

    if (argc < 2) {
        printf("Provide a file name!!!\n");
        return -1;
    }

    fd = open(argv[1], O_CREAT|O_WRONLY|O_APPEND, 0644);
    n = read(0, buffer, MAX);
    buffer[strcspn(buffer, "\n")] = 0;          // removing trailing \n

    while (strcmp(buffer, "-1") != 0) {
        write(fd, buffer, n);
        write(fd, newLine, 1);                  // going to the new line
        n = read(0, buffer, MAX);
        buffer[strcspn(buffer, "\n")] = 0;      // removing trailing \n
    }

    return 0;
}

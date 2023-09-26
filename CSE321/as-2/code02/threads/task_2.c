#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

#define LEN 5

void *thread_function(void *arg) {
    int *x = arg;
    int start = 1;

    while (start<=LEN) {
        printf("Thread %d prints %d\n", *x, 5*(*x)+start);
        start++;
    }
}

int main() {

    pthread_t th[LEN];

    for (int i=0; i<LEN; i++) {
        pthread_create(&th[i], NULL, thread_function, &i);
        pthread_join(th[i], NULL);
    }

    return 0;
}

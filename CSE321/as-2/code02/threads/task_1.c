#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

#define LEN 5

void *thread_function(void *arg) {
    int *x = arg;
    printf("thread-%d running\n", *x + 1);
}

int main() {

    pthread_t th[LEN];

    for (int i=0; i<LEN; i++) {
        pthread_create(&th[i], NULL, thread_function, &i);
        pthread_join(th[i], NULL);
        printf("thread-%d closed\n", i + 1);
    }

    return 0;
}

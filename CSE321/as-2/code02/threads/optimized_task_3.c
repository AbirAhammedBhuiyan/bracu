#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <stdlib.h>
#include <string.h>

#define LEN 3


typedef struct thread {
    pthread_t thread_id;
    char *user_name;
    int sum;
} ThreadData;


int frqMatch(ThreadData *thread) {

    int max = -1;

    for (int i=0; i<LEN; i++) {
        int count = 0;
        for (int j=0; j<LEN; j++) {
            if (thread[j].sum == thread[i].sum) {
                count++;
            }
        }

        if (max < count) 
            max = count;
    }

    return max;
}


void *matchPrinter(void *arg) {

    int *match = (int *)arg;

    switch (*match) {
        case 3:
            printf("Youreka\n");
            break;
        case 2:
            printf("Miracle\n");
            break;
        case 1:
            printf("Hasta la vista\n");
            break;
        default:
            printf("Error\n");
            break;
    }
}


void *asciiSum(void *arg) {

    ThreadData *thread = (ThreadData *) arg;

    char *name = thread->user_name;

    int sum = 0;

    for (int i=0; name[i]!='\0'; ++i) {
        sum += name[i];
    }

    thread->sum = sum;
}


int main() {

    ThreadData thread[LEN];
    pthread_t print_thread;

    thread[0].user_name = "cai00en";
    thread[1].user_name = "eniac00";
    thread[2].user_name = "altair00";
    // should print 'Miracle'

    for (int i=0; i<LEN; i++) {
        pthread_create(&(thread[i].thread_id), NULL, asciiSum, (void *)&(thread[i]));
        pthread_join(thread[i].thread_id, NULL);
    }

    // finding maximum possible match number
    int match = frqMatch(thread);

    // printing thread
    if (match != -1) {
        pthread_create(&print_thread, NULL, matchPrinter, (void *)&match);
        pthread_join(print_thread, NULL);
    }

    return 0;

}



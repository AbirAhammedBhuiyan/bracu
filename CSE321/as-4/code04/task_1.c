#include <pthread.h>   
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 10 //producers and consumers can produce and consume upto MAX
#define BUFLEN 6
#define NUMTHREAD 2      /* number of threads */

void * consumer(int *id);
void * producer(int *id);

char buffer[BUFLEN];
char source[BUFLEN+1]; //from this array producer will store it's production into buffer
int pCount = 0;
int cCount = 0;
int count = 0;       // total count of how many resources are currently in the buffer (aka the critical variable)
int buflen;

//initializing pthread mutex and condition variables
pthread_mutex_t count_mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t nonEmpty  = PTHREAD_COND_INITIALIZER;
pthread_cond_t full  = PTHREAD_COND_INITIALIZER;
int thread_id[NUMTHREAD]  = {0,1};
int i = 0; 
int j = 0;

int main() {
    int i;
    /* define the type to be pthread */
    pthread_t thread[NUMTHREAD];

    strcpy(source,"abcdef");
    buflen = strlen(source);
    /* create 2 threads*/
    /* create one consumer and one producer */
    /* define the properties of multi threads for both threads  */
    
    for (i=0; i<NUMTHREAD; i++) {
        if (i == 0)
            pthread_create(&thread[i], NULL, (void *) &producer, (void *) &thread_id[i]);
        else
            pthread_create(&thread[i], NULL, (void *) &consumer, (void *) &thread_id[i]);
    }

    for (i=0; i<NUMTHREAD; i++) {
        pthread_join(thread[i], NULL);
    }

    pthread_mutex_destroy(&count_mutex);
    pthread_cond_destroy(&nonEmpty);
    pthread_cond_destroy(&full);

    return 0;
}


void * producer(int *id) {
	/*
1. Producer stores the values in the buffer (Here copies values from source[] to buffer[]).
2. Use mutex and thread communication (wait(), sleep() etc.) for the critical section.
3. Print which producer is storing which values using which thread inside the critical section.
4. Producer can produce up to MAX
*/
    for (i=0; i<MAX; i++) {
        pthread_mutex_lock(&count_mutex);

        if (count > BUFLEN) 
            exit(1); // overflow 

        while (count == BUFLEN)
            pthread_cond_wait(&nonEmpty, &count_mutex);

        buffer[pCount] = source[pCount];
        printf("%d produced %c by Thread %d\n", i, buffer[pCount], *((int *) id));
        pCount = (pCount+1)%BUFLEN;
        count++;
        pthread_mutex_unlock(&count_mutex);
        pthread_cond_signal(&full);
    }
}

void * consumer(int *id) {
   	/*
1. Consumer takes out the value from the buffer and makes it empty.
2. Use mutex and thread communication (wait(), sleep() etc.) for critical section
3. Print which consumer is taking which values using which thread inside the critical section.
4. Consumer can consume up to MAX
*/
    for (j=0; j<MAX; j++) {
        pthread_mutex_lock(&count_mutex);

        if (count < 0)
            exit(1); // underflow
        
        while (count == 0) 
            pthread_cond_wait(&full, &count_mutex);

        printf("%d consumed %c by Thread %d\n", j, buffer[cCount], *((int *) id));
        cCount = (cCount+1)%BUFLEN;
        count--;
        pthread_mutex_unlock(&count_mutex);
        pthread_cond_signal(&nonEmpty);
    }
}

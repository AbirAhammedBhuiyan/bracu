#include "utils/utils.h"

static void SRTF(process_t * process, int len) {

    // sorting the process array according to the arrival time
    qsort(process, len, sizeof(process[0]), SortAT);

    // defining queue heads
    head_t_int elapsedTime;
    head_t_int intervals;
    head_t_int readyQ;
    head_t_str processNames;

    // initializing queues
    TAILQ_INIT(&elapsedTime);
    TAILQ_INIT(&intervals);
    TAILQ_INIT(&readyQ);
    TAILQ_INIT(&processNames);

    int bt[len];                // burst time array for temporary use
    int start_time = 0;
    int elapsed_time = 0;
    int cp = 0;                 // current process
    int new_cp = -1;
    int total_process_finished = 0;

    // copying all the processes burst time to bt[]
    for (int i=0; i<len; i++) {
        bt[i] = process[i].bt;
    }

    EnQueueINT(&intervals, start_time);
    EnQueueINT(&readyQ, cp);
    NewProcess(process, len, start_time, start_time, &readyQ, cp);
    SortQueueINT_Arr(bt, &readyQ);
    

    while (!TAILQ_EMPTY(&readyQ) && total_process_finished<len) {

        cp = Dequeue(&readyQ);
        EnQueueINT(&readyQ, cp);
        SortQueueINT_Arr(bt, &readyQ);

        if (start_time < process[cp].at) {

            elapsed_time = process[cp].at - start_time;
            start_time += elapsed_time;

            // context switch
            EnQueueINT(&elapsedTime, elapsed_time);
            EnQueueSTR(&processNames, "-");
            EnQueueINT(&intervals, start_time);
            EnQueueINT(&readyQ, cp);
            SortQueueINT_Arr(bt, &readyQ);

        } else {

            start_time++;
            elapsed_time++;
            bt[cp]--;


            NewProcess(process, len, start_time-1, start_time, &readyQ, cp);
            SortQueueINT_Arr(bt, &readyQ);

            if (bt[cp] == 0) {

                total_process_finished++;
                process[cp].ct = start_time;
                // context switch
                EnQueueINT(&elapsedTime, elapsed_time);
                EnQueueSTR(&processNames, process[cp].pid);
                EnQueueINT(&intervals, start_time);
                Dequeue(&readyQ); 
                elapsed_time = 0;

            } else {

                new_cp = Dequeue(&readyQ);
                EnQueueINT(&readyQ, new_cp);
                SortQueueINT_Arr(bt, &readyQ);

                if (new_cp != -1 && new_cp != cp) {

                    // context switch
                    EnQueueINT(&elapsedTime, elapsed_time);
                    EnQueueSTR(&processNames, process[cp].pid);
                    EnQueueINT(&intervals, start_time);
                    SortQueueINT_Arr(bt, &readyQ);
                    elapsed_time = 0;

                }
            }
        }
    }

    // calculating waiting times and turnaround times of all process using the completion time
    for(int i=0; i<len; i++) {
        process[i].tat = process[i].ct - process[i].at;
        process[i].wt = process[i].tat - process[i].bt;
    }

    printf("\n\n\tSRTF [Shortest Remaining Time First] \n\n\n");

    // making the table
    TableMaker(process, len, 0);

    // freeing memory allocations of all the queues 
    FreeQueueINT(&elapsedTime);
    FreeQueueINT(&intervals);
    FreeQueueINT(&readyQ);
    FreeQueueSTR(&processNames);

}

int main() {

    /*************************** SRTF ********************/

     int length = 5; 
     char *pid[] = {"P1", "P2", "P3", "P4", "P5"}; 
     int at[] = {0, 2, 3, 4, 5}; 
     int bt[] = {5, 2, 7, 4, 5}; 

     process_t process[length]; 

     for (int i=0; i<length; i++) { 
         strcpy(process[i].pid, pid[i]); 
         process[i].at = at[i]; 
         process[i].bt = bt[i]; 
     } 

     SRTF(process, length); 

     return 0;

}

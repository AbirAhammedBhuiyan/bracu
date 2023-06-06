#include <stdio.h>
#include <stdlib.h>

int main() {

    int n = 6; // Number of processes
    int m = 4; // Number of resources

    int alloc[6][4] = { { 0, 1, 0, 3 }, // P0 // Allocation Matrix
                        { 2, 0, 0, 3 }, // P1
                        { 3, 0, 2, 0 }, // P2
                        { 2, 1, 1, 5 }, // P3
                        { 0, 0, 2, 2 }, // P4
                        {1, 2 , 3, 1 } }; //P5

    int max[6][4] = { { 6, 4, 3, 4 }, // P0 // MAX Matrix
                      { 3, 2, 2, 4 }, // P1
                      { 9, 1, 2, 6 }, // P2
                      { 2, 2, 2, 8 }, // P3
                      { 4, 3, 3, 7 }, // P4
                      { 6, 2 , 6, 5 } }; //P5

    int avail[4] = { 2, 2, 2, 1 }; //Available resources


    int completed[n], sequence[n], index = 0;

    for (int k = 0; k < n; k++) {
        completed[k] = 0;       // is the process complete -> f[k] : 0 -> not finished , 1 -> finished
    }

    int need[n][m];     // more need to finish a particular process

    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++)
            need[i][j] = max[i][j] - alloc[i][j];
    }

    for (int k=0; k<n; k++) {
        for (int i=0; i<n; i++) {

            if (completed[i] == 0) {

                int flag = 0;

                for (int j=0; j<m; j++) {

                    if (need[i][j] > avail[j]){
                        flag = 1;
                        break;
                    }

                }
 
                if (flag == 0) {

                    sequence[index++] = i;

                    for (int y=0; y<m; y++) {
                        avail[y] += alloc[i][y];
                    }

                    completed[i] = 1;

                }

            }
        }
    }
       
    int flag = 1;
           
    for (int i=0; i<n; i++) {
        if (completed[i]==0) {
            flag=0;
            printf("Deadlock Ahead\n");
            break;
        }
    }

    if (flag) {
        for (int i=0; i<n; i++) {
            if (i!=n-1) {
                printf("P%d -> ", sequence[i]);
            } else {
                printf("P%d\n", sequence[i]);
            }
        }
    }

    return 0;

}

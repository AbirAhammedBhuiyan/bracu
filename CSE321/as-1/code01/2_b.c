#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 1000

void TrimExtraSpaces(char *input_file, char *output_file) {

    FILE *in = fopen(input_file, "r");
    if (in == NULL) {
        perror("Error opening input file");
        exit(1);
    }

    FILE *out = fopen(output_file, "w");
    if (out == NULL) {
        perror("Error opening output file");
        fclose(in);
        exit(1);
    }

    char string[MAX];

    fgets(string, MAX, in);

    int i = 0, j = 0;

    while (string[i] != '\0') {
        while (string[i] == ' ' && string[i + 1] == ' ') {
            ++i;
        }
        string[++j] = string[++i];
    }

    string[j] = '\0';

    fputs(string, out);

    fclose(in);
    fclose(out);
}

int main() {

    TrimExtraSpaces("input.txt", "output.txt");

    return 0;

}


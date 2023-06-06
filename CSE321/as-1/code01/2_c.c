#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX 200

void Printer(int upper_flag, int lower_flag, int digit_flag, int special_flag) {

    char error[MAX] = "";

    if (!lower_flag)
        strcat(error, "Lowercase character missing, ");
    if (!upper_flag)
        strcat(error, "Uppercase character missing, ");
    if (!digit_flag)
        strcat(error, "Digit missing, ");
    if (!special_flag)
        strcat(error, "Special character missing, ");

    if(upper_flag && lower_flag && digit_flag && special_flag) {
        printf("OK\n");
    }
    else {
        error[strlen(error) - 2] = '\0';
        printf("%s\n", error);
    }
}

void PassChecker(char *pass) {

    int upper_flag, lower_flag, digit_flag, special_flag;
    upper_flag = lower_flag = digit_flag = special_flag = 0;
    
    for (int i=0; pass[i] != '\0'; i++) {
        if (isupper(pass[i])) 
            upper_flag = 1;
        if (islower(pass[i]))
            lower_flag = 1;
        if (isdigit(pass[i]))
            digit_flag = 1;
        if (pass[i] == '_' || pass[i] == '$' || pass[i] == '#' || pass[i] == '@')
            special_flag = 1;
    }

    Printer(upper_flag, lower_flag, digit_flag, special_flag);
    
}


int main() {

    char pass[MAX];    

    printf("Enter the password: ");
    fgets(pass, MAX, stdin);

    pass[strcspn(pass, "\n")] = 0; // removing trailing \n

    PassChecker(pass);
    
    return 0;
}

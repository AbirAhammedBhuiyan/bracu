#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 200

int isPalindrome(char *string) {

    char *rev = string + strlen(string) - 1;

    while(string < rev) {

        if(*string != *rev) 
            return 0;

        ++string;
        --rev;
    }

    return 1;
}

int main() {

    char str[MAX];

    printf("Enter a string: ");

    fgets(str, MAX, stdin);

    str[strcspn(str, "\n")] = 0; // removing trailing `\n`

	printf("%s\n", isPalindrome(str) ? "Palindrome" : "Not Palindrome");

	return 0;
}


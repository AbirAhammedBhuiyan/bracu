#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 200

int main() {

    char email[MAX];
    char *domain = "sheba.xyz";

    printf("Please enter the email to check: ");
    fgets(email, MAX, stdin);

    email[strcspn(email, "\n")] = 0; // removing trailing `\n`
    
    printf("Email address is %s\n", strstr(email, domain) ? "okay" : "outdated");
    
    return 0;

}

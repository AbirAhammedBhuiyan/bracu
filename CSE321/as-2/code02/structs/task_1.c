#include <stdio.h>
#include <stdlib.h>

#define LEN 3

typedef struct items {
    int quantity;
    int price;
} items_t;


int main() {

    items_t item_arr[LEN]; 
    // item_arr[LEN] -> struct array
    // item_arr[0] -> paratha
    // item_arr[1] -> vegetables
    // item_arr[2] -> mineral water
    
    char item_names[LEN][30] = {"Paratha", "Vegetables", "Mineral Water"};
    int total_bill = 0;
    int num_of_people = 0;

    for (int i=0; i<LEN; i++) {
        printf("Quantity Of %s: ", item_names[i]);
        scanf("%d", &item_arr[i].quantity);
        printf("Unit Price: ");
        scanf("%d", &item_arr[i].price);

        total_bill += item_arr[i].quantity*item_arr[i].price;
    }

    printf("Number of Peopele: ");
    scanf("%d", &num_of_people);

    if (num_of_people > 0) {
        printf("Individual people will pay: %.2f tk\n", (float)(total_bill/num_of_people));
    } else {
        printf("Error\n");
    }

    return 0;

}

#include <stdio.h>

int main() {
    // Array of character arrays (strings)
    char *listOfUsers[] = {"User1", "User2", "User3"};
    
    // Print the list using a for loop
    for (int i = 0; i < 3; i++) {
        printf("%s\n", listOfUsers[i]);
    }
    
    return 0;
}
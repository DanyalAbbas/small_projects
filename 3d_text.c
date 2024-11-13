#include <stdio.h>

// Define ANSI color codes
#define RESET "\033[0m"
#define RED "\033[31m"
#define GREEN "\033[32m"
#define YELLOW "\033[33m"
#define BLUE "\033[34m"
#define BOLD "\033[1m"
#define UNDERLINE "\033[4m"

int main() {
    printf(BOLD "This is bold text\n" RESET);
    printf(RED "This is red text\n" RESET);
    printf(GREEN "This is green text\n" RESET);
    printf(YELLOW "This is yellow text\n" RESET);
    printf(BLUE UNDERLINE "This is blue underlined text\n" RESET);

    return 0;
}

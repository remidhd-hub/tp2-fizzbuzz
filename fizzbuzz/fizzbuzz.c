
int main () {
    char *fizzbuzz = "FizzBuzz,";
    char *fizz = "Fizz,";
    char *buzz = "Buzz,";

    for (int i = 1 ; i < 101; i++) {
        if ((i%3 == 0) && (i%5 == 0)) {
            printf("%s ", fizzbuzz);
        }
        else if ((i%3 == 0) && (i%5 != 0)) {
            printf("%s ", fizz);
        }
        else if ((i%5 == 0) && (i%3 != 0))  {
            printf("%s ", buzz);
        }
        else {
            printf("%d, ", i);
        }
    }

    return 0;
}

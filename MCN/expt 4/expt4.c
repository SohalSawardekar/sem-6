#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void visualize(char *encoded, int length)
{
    printf("\nSignal Visualization:\n");

    // **High Signals**
    for (int i = 0; i < 2 * length; i++)
    {
        if (encoded[i] == '1')
            printf("---");
        else
            printf("   "); // Space for low signal
    }
    printf("\n");

    // **Transition Line**
    for (int i = 0; i < 2 * length; i++)
    {
        if (i > 0 && encoded[i - 1] != encoded[i])
            printf("|  "); // Transition marker
        else
            printf("   "); // Space for non-transition
    }
    printf("\n");

    // **Low Signals**
    for (int i = 0; i < 2 * length; i++)
    {
        if (encoded[i] == '0')
            printf("---");
        else
            printf("   "); // Space for high signal
    }
    printf("\n");
}

// Manchester encoding
void manchester(char *input, char *output, int length)
{
    printf("Manchester Encoding:\n");

    for (int i = 0; i < length; i++)
    {
        if (input[i] == '0')
        {
            // For '1': High then Low
            output[2 * i] = '1';
            output[2 * i + 1] = '0';
            printf("10 ");
        }
        else if (input[i] == '1')
        {
            // For '0': Low then High
            output[2 * i] = '0';
            output[2 * i + 1] = '1';
            printf("01 ");
        }
        else
        {
            printf("\nInvalid character in input!\n");
            return;
        }
    }
    output[2 * length] = '\0'; // Null-terminate
    printf("\n");
}

// Differential Manchester encoding
void differentialManchester(char *input, char *output, int length)
{
    printf("Differential Manchester Encoding:\n");

    int lastState = 1; // Start with a '1' (can also start with 0, as long as consistent)

    for (int i = 0; i < length; i++)
    {
        if (input[i] == '0')
        {
            // Same as lastState -> Opposite in the middle -> Flip lastState after
            output[2 * i] = lastState + '0';
            output[2 * i + 1] = (lastState ^ 1) + '0';

            printf("%c%c ", output[2 * i], output[2 * i + 1]);

            lastState ^= 1; // Flip for the next iteration
        }
        else if (input[i] == '1')
        {
            // Flip lastState first -> Then use it
            lastState ^= 1;

            output[2 * i] = lastState + '0';
            output[2 * i + 1] = (lastState ^ 1) + '0';

            printf("%c%c ", output[2 * i], output[2 * i + 1]);

            // Flip again for next iteration
            lastState ^= 1;
        }
        else
        {
            printf("\nInvalid character in input!\n");
            output[0] = '\0'; // Clear output
            return;
        }
    }

    output[2 * length] = '\0'; // Null-terminate
    printf("\n");
}

int main()
{
    char input[1000];
    char outputManchester[2000];
    char outputDifferentialManchester[2000];

    printf("Enter binary string: ");
    scanf("%s", input);

    int length = strlen(input);

    // 1) Manchester
    manchester(input, outputManchester, length);
    visualize(outputManchester, length);

    printf("\n\n");
    // 2) Differential Manchester
    differentialManchester(input, outputDifferentialManchester, length);
    visualize(outputDifferentialManchester, length);

    return 0;
}

/*
Output:

Enter binary string: 0110101001
Manchester Encoding:
01 10 10 01 10 01 10 01 01 10

Signal Visualization:
   ------   ---      ------      ------      ---   ------
   |     |  |  |     |     |     |     |     |  |  |     |
---      ---   ------      ------      ------   ---      ---


Differential Manchester Encoding:
10 10 10 01 01 10 10 01 10 10

Signal Visualization:
---   ---   ---      ---   ------   ---      ------   ---
   |  |  |  |  |     |  |  |     |  |  |     |     |  |  |
   ---   ---   ------   ---      ---   ------      ---   ---

*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

const char flag[9] = "01111110"; // Added null terminator

void inputData(char **packet)
{
    char tempdata[1000];
    printf("Enter the data: ");
    scanf("%999s", tempdata); // Added limit for safety

    // +1 for null terminator, +16 for flags
    *packet = (char *)malloc(strlen(tempdata) + 17);
    if (*packet == NULL)
    {
        printf("Memory allocation failed!\n");
        exit(1);
    }
    strcpy(*packet, tempdata);
    printf("\nData: %s\n", *packet);
}

void addHeadTrail(char *packet)
{
    size_t dataLen = strlen(packet);
    char *tempPacket = (char *)malloc(dataLen + 1);
    if (tempPacket == NULL)
    {
        printf("Memory allocation failed!\n");
        exit(1);
    }

    strcpy(tempPacket, packet);

    // Make space at start for flag
    memmove(packet + 8, packet, dataLen + 1);
    // Add head flag
    memcpy(packet, flag, 8);
    // Add tail flag
    memcpy(packet + dataLen + 8, flag, 8);
    packet[dataLen + 16] = '\0';

    free(tempPacket);
}

void bitStuffing(char *packet)
{
    size_t len = strlen(packet);
    char *result = (char *)malloc(2 * len); // Worst case scenario
    if (result == NULL)
    {
        printf("Memory allocation failed!\n");
        exit(1);
    }

    int j = 0;
    int consecutive_ones = 0;

    // Copy first flag
    memcpy(result, packet, 8);
    j = 8;

    // Process data portion
    for (size_t i = 8; i < len - 8; i++)
    {
        result[j++] = packet[i];
        if (packet[i] == '1')
        {
            consecutive_ones++;
            if (consecutive_ones == 5)
            {
                result[j++] = '0'; // Add stuffing bit
                consecutive_ones = 0;
            }
        }
        else
        {
            consecutive_ones = 0;
        }
    }

    // Copy end flag
    memcpy(result + j, packet + len - 8, 8);
    j += 8;
    result[j] = '\0';

    strcpy(packet, result);
    free(result);
}

int main()
{
    char *packet = NULL;
    inputData(&packet);
    addHeadTrail(packet);
    bitStuffing(packet);
    printf("\nFinal data: %s\n", packet);
    free(packet);
    return 0;
}
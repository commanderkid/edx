#include <stdio.h>

int main(void)
{
    //scaning first digit
    int numOfexamples = 0;
     //massive for saving integers
    char ansver[11] = {' ', ' ', ' ', ' ', ' ', ' ', 
                       ' ', ' ', ' ', ' ', ' '};
    scanf("%d", &numOfexamples);
    for(int ex = 0; ex < numOfexamples; ex++) //reading lines of examples
    {
        int so[9] = {0};
        char xo[] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};
        scanf("%d %d %d %d %d %d %d %d %d", &so[0], &so[1], &so[2], 
                                            &so[3], &so[4], &so[5], 
                                            &so[6], &so[7], &so[8]);
                                         
        for(int i = 0; i < 9; i++) // 9 is number of cells in x-0
        {
            xo[so[i] - 1] = (i % 2) == 0 ? 'X' : '0'; /*[so[i] - 1] it is index 
            of element in massive xo, where so[i] number from input*/
            if  ((xo[0] == xo[1] && xo[0] == xo[2]) ||
                 (xo[3] == xo[4] && xo[3] == xo[5]) ||
                 (xo[6] == xo[7] && xo[6] == xo[8]) ||
                 (xo[0] == xo[3] && xo[0] == xo[6]) ||
                 (xo[1] == xo[4] && xo[1] == xo[7]) ||
                 (xo[2] == xo[5] && xo[2] == xo[8]) ||
                 (xo[0] == xo[4] && xo[0] == xo[8]) ||
                 (xo[2] == xo[4] && xo[2] == xo[6]))
            {
                ansver[ex] = i + 1;
                break;
            }
            else if(i >= 8)
            {
                ansver[ex] = 0;
                break;
            }
        }
        //we have array of char, and we can devide array in to 8 parts
    }
    for(int i = 0; i < 11; i++)
    {
        if(ansver[i] != ' ') printf("%d ", ansver[i]);
    }
    
    /*
    for(int i = 0; i < 9; i++)
    {
        if (i % 3 == 0) printf("\n");
        printf("%4c", xo[i]);
    }
    printf("\n");
    return 0;
    */
}

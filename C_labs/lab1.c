#include <stdio.h>

int main()
{
    int n, counter = 0;


    int Nums[100];
    do
    {
        printf("Vvedite kolichestvo elementov: ");
        scanf("%d", &n);
    } while(n <= 0);

    printf("Vvedite elementi cherez probel: \n");
    for(int i = 0; i < n; i++)
    {
        int num;
        scanf("%d", &num);
        Nums[i] = num;
    }
    for(int i = 0; i < n; i++)
    {
        if(Nums[i] % 3 == 0)
        {
            counter++;
        }
    }

    if(counter == 0)
    {
        printf("Kratnih trem net \n");
    }
    else if(counter)
    {
        printf("Kratnih trem: %d", counter);
    }

    return 0;
}

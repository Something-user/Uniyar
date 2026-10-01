#include <stdio.h>
#define MAX_SIZE 100

int main()
{
    int n, counter = 0, sum = 0;
    int formscan;


    int Nums[MAX_SIZE];
    printf("Vvedite kolichestvo elementov: ");
    formscan = scanf_s("%d", &n);
    if (!formscan) {
        printf("Vvedite chislo");
        return 1;
    }

    int f;
    printf("Vvedite elementi cherez probel: \n");
    for (int i = 0; i < n; i++)
    {
        int num;
        f = scanf_s("%d", &num);
        if (!f) {
            printf("Vvodite chisla");
            return 1;
        }
        Nums[i] = num;
    }

    for (int i = 0; i < n; i++)
    {
        if (Nums[i] % 3 == 0)
        {
            counter++;
            sum += Nums[i];
        }
    }

    if (counter == 0)
    {
        printf("Kratnih trem net \n");
    }
    else if (counter)
    {
        printf("Kratnih trem: %d\n", counter);
        printf("Summa elementov kratnih trem: %d", sum);
    }

    return 0;
}

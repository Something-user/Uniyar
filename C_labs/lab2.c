#include <stdio.h>
#define MAX_SIZE 20

void input_matrix(int array[MAX_SIZE][MAX_SIZE], int n, int m){ // Функция ввода матрицы
    printf("Vvedite matritsu: ");
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            scanf("%d", &array[i][j]);
        }
    }
}

/*
int sum(int array[MAX_SIZE], int summa, int n){
    for(int i = 0, i < n; i++){
        summa += array[i];
    }
    return summa;
}
*/

/*
void output_matrix(int array[MAX_SIZE][MAX_SIZE], int n, int m){ // Функция вывода матрицы
    for(int i = 0; i < n; i++){
        for(int j = 0; i < m; j++){
            printf("printf("%3d", array[i][j])");
        }
        printf("\n");
    }
}
*/


int sum_str_is_equal(int array[MAX_SIZE][MAX_SIZE], int n, int m){
    int summa = 0;
    for(int i = 0; i < (n-1); i++){
        int sum1 = 0;
        int sum2 = 0;
        for(int j = 0; j < m; j++){
            sum1 += array[i][j];
            sum2 += array[i+1][j];
        }
        if(sum1 != sum2){
            return 1;
        }
        else{
            summa = sum2;
        }
    }
    return summa;
}

/*
int sum_col_is_equal(int array[MAX_SIZE][MAX_SIZE], int n, int m){
    int summa = 0;
    for(int i = 0; i < n; i++){
        int sum1 = 0;
        int sum2 = 0;
        for(int j = 0; j < m-1; j++){
            sum1 += array[j][i];
            sum2 += array[j+1][i];
        }
        if(sum1 != sum2){
            return 1;
        }
        else{
            summa = sum2;
        }
    }
    return summa;
}
*/

int main()
{
    int Matrix[MAX_SIZE][MAX_SIZE]; // Создание матрицы 20*20
    int n, m; // Создание пользовательских размеров
    int formscan; // Создание переменной для проверки ввода данных

    do{                                      // Проверка на корректность вводимых данных
        printf("Vvedite razmer matritsi: ");
        formscan = scanf("%d %d", &n, &m);
        if(formscan != 2){
            printf("Vvedite tcelie chisla");
            return 1;
        }
        if(m != n){
            printf("Matritsa doljna bit kvadratnoy\n");
        }

    } while(n <= 0 || m <= 0 || m != n);

    input_matrix(Matrix, n, m); // Заполнение матрицы

/*
    int sum_str_one = 0, sum_str_two = 0;

    for(int i = 0; i< n; i++)
    {
        int summa = 0;
        for(int j = 0; j < m; j++)
        {
            summa += Matrix[i][j];
        }
        sum_str_two = sum_str_one;
        sum_str_one = summa;
        if(sum_str_two != 0 && sum_str_two == sum_str_one){
            sum_str_two = sum_str_one;
            printf("yes");
        }
        else if(sum_str_two != 0 && sum_str_one != sum_str_two){
            printf("Matritsa ne yavlyaetsa magicheskim kvadratom");
            return 1;
        }
    }
*/
    //output_matrix(Matrix, n, m);

    for(int i = 0; i < n; i++){
        int sum1 = 0;
        int sum2 = 0;
        for(int j = 1; j < m; j++){
            sum1 += Matrix[j-1][i];
            printf("%d\n", sum1);
            sum2 += Matrix[j][i];
            printf("V%d\n", sum2);
        }
        //printf("%d\n", sum1);
        //printf("%d", sum2);
        if(sum1 != sum2){
            return 1;
        }
        else{
            printf("Yes");
        }
    }
/*
    printf("%d\n", sum_str_is_equal(Matrix, n, m));
    printf("%d", sum_col_is_equal(Matrix, n, m));
*/
}

/*
*/

#include <stdio.h>
#define MAX_SIZE 20

int input_matrix(int array[MAX_SIZE][MAX_SIZE], int n, int m); /* Функция ввода матрицы */

/*
int sum(int array[MAX_SIZE], int summa, int n){
    for(int i = 0, i < n; i++){
        summa += array[i];
    }
    return summa;
}
*/

int sum_str_is_equal(int array[MAX_SIZE][MAX_SIZE], int n, int m); /* Функция суммы строк */
int sum_col_is_equal(int array[MAX_SIZE][MAX_SIZE], int n, int m); /* Функция суммы столбцов */
int sum_direct_diag(int array[MAX_SIZE][MAX_SIZE], int n, int m); /* Функция суммы прямой диагонали */
int sum_revers_diag(int array[MAX_SIZE][MAX_SIZE], int n, int m); /* Функция суммы обратной диагонали */

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

int main()
{
    int Matrix[MAX_SIZE][MAX_SIZE]; /* Создание матрицы 20*20 */
    int n, m; // Создание пользовательских размеров
    int formscan; // Создание переменной для проверки ввода данных

    do{                                      // Проверка на корректность вводимых данных
        printf("Enter the matrix size: ");
        formscan = scanf("%d %d", &n, &m);
        if(formscan != 2){
            printf("Enter whole numbers");
            return 1;
        }
        if(m != n){
            printf("Matritsa doljna bit kvadratnoy\n");
        }

    } while(n <= 0 || m <= 0 || m != n);
    if(input_matrix(Matrix, n, m) == 1)
    {
        printf("Enter numbers, not letters");
        return 1;
    }
    input_matrix(Matrix, n, m); // Заполнение матрицы

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

}

int input_matrix(int array[MAX_SIZE][MAX_SIZE], int n, int m){
    printf("Enter the matrix: \n");
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(scanf("%d", &array[i][j]) != 1)
            {
                return 1;
            }
        }
    }
    return 0;
}

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

int sum_col_is_equal(int array[MAX_SIZE][MAX_SIZE], int n, int m){
    int summa = 0;
    for(int i = 0; i < n-1; i++)
    {
        int sum1 = 0;
        int sum2 = 0;
        for(int j = 0; j < m; j++)
        {
            sum1 += array[j][i];
            sum2 += array[j][i+1];
        }
        if(sum1 != sum2)
        {
            return 1;
        }
        else
        {
            summa = sum1;
        }
    }
    return summa;
}

int sum_direct_diag(int array[MAX_SIZE][MAX_SIZE], int n, int m){
    int summa = 0;
    for(int i = 0; i < n; i++)
    {
        summa += array[i][i];
    }
    return summa;
}

int sum_revers_diag(int array[MAX_SIZE][MAX_SIZE], int n, int m){
    int summa = 0;
    int j = m-1;
    for(int i = 0; i < n; i++)
    {
        summa += array[i][j];
        j--;
    }
    return summa;
}


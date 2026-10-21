/* Данная программа выполнена студентом ЯРГУ имени П.Г.Демидова направления программная инженерия Стрижовым Михаилом Николаевичем.
 * Предназначение программы: определить является ли введенная с клавиатуры матрица магическим квадратом
 * (суммы по всем строкам, столбцам и обеим диагоналям равны)
*/

#include <stdio.h>
#define MAX_SIZE 20

int input_matrix(int array[MAX_SIZE][MAX_SIZE], int n, int m); /* Функция ввода матрицы */


int sum_str_is_equal(int array[MAX_SIZE][MAX_SIZE], int n, int m); /* Функция проверки равенства сумм строк */
int sum_col_is_equal(int array[MAX_SIZE][MAX_SIZE], int n, int m); /* Функция проверки равенства сумм столбцов */
int sum_direct_diag(int array[MAX_SIZE][MAX_SIZE], int n, int m); /* Функция суммы прямой диагонали */
int sum_revers_diag(int array[MAX_SIZE][MAX_SIZE], int n, int m); /* Функция суммы обратной диагонали */
int sum_diag_is_equal(int sum_diag1, int sum_diag2); /* Функция проверки равенства диагоналей */


int main(void)
{
    int Matrix[MAX_SIZE][MAX_SIZE]; /* Создание матрицы 20*20 */
    int n, m; /* Создание пользовательских размеров */
    int formscan; /* Создание переменной для проверки ввода данных */

    do{                                      /* Проверка на корректность вводимых данных */
        printf("Enter the matrix size: ");
        formscan = scanf("%d %d", &n, &m);
        if(formscan != 2){
            printf("Enter whole numbers");
            return 1;
        }
        if(m != n){
            printf("The matrix must be square\n");
        }

    } while(n <= 0 || m <= 0 || m != n);

    printf("Enter the matrix: \n");
    if(input_matrix(Matrix, n, m) == 1){
        printf("Enter whole numbers, not letters");
        return 1;
    }

    int sum_str = sum_str_is_equal(Matrix, n, m);
    int sum_col = sum_col_is_equal(Matrix, n, m);
    int sum_diag1 = sum_direct_diag(Matrix, n, m);
    int sum_diag2 = sum_revers_diag(Matrix, n, m);

    int sum_diag = sum_diag_is_equal(sum_diag1, sum_diag2);

    if(sum_str == 1 || sum_col == 1 || sum_diag == 1){
    /* Проверка, что суммы строк равны, суммы столбцов равны, суммы диагоналей равны */
        printf("The matrix is not a magic square");
        return 1;
    }

    if(sum_str == sum_col && sum_col == sum_diag){ /* Проверка совпадения сумм строк, столбцов и диагоналей */
        printf("Magic square");
    }
    else{
        printf("The matrix is not a magic square");
        return 1;
    }

    return 0;
}

int input_matrix(int array[MAX_SIZE][MAX_SIZE], int n, int m){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(scanf("%d", &array[i][j]) != 1){
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
    for(int i = 0; i < n-1; i++){
        int sum1 = 0;
        int sum2 = 0;
        for(int j = 0; j < m; j++){
            sum1 += array[j][i];
            sum2 += array[j][i+1];
        }
        if(sum1 != sum2){
            return 1;
        }
        else{
            summa = sum1;
        }
    }
    return summa;
}

int sum_direct_diag(int array[MAX_SIZE][MAX_SIZE], int n, int m){
    int summa = 0;
    for(int i = 0; i < n; i++){
        summa += array[i][i];
    }
    return summa;
}

int sum_revers_diag(int array[MAX_SIZE][MAX_SIZE], int n, int m){
    int summa = 0;
    int j = m-1;
    for(int i = 0; i < n; i++){
        summa += array[i][j];
        j--;
    }
    return summa;
}

int sum_diag_is_equal(int sum_diag1, int sum_diag2){
    if(sum_diag1 != sum_diag2){
        return 1;
    }
    else{
        return sum_diag1;
    }
}

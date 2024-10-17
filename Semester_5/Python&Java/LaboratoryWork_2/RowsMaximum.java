//7. Задача: Найти максимальный элемент в каждой строке двумерного массива.
//Условие: Напишите метод, который принимает двумерный массив целых чисел и возвращает
//одномерный массив, содержащий максимальный элемент из каждой строки исходного массива.

import java.util.Scanner;

public class RowsMaximum {
    public static void main(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите кол-во строк в матрице:");
        int n = scanner.nextInt();
        System.out.println("Введите кол-во столбцов в матрице:");
        int m = scanner.nextInt();
        System.out.println("Введите матрицу: ");
        int[][] Matrix = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                Matrix[i][j] = scanner.nextInt();
            }
        }

        int [] Maximum = new int[n];
        //Ищем максимальные элемнты каждой строки и выписываем их в отдельный массив
        for (int i = 0; i < n; i++) {
            int max = -100000;
            for (int j = 0; j < m; j++) {
                max = Math.max(Matrix[i][j], max);
            }
            Maximum[i] = max;
        }

        //Вывод
        System.out.print("Result: ");
        for (int i = 0; i < n; i++) {
            System.out.print(Maximum[i] + " ");
        }
        System.out.println();
    }
}

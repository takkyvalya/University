//6. Задача: Найти сумму всех элементов в двумерном массиве.
//Условие: Напишите метод, который принимает двумерный массив целых чисел и возвращает их
//сумму.

import java.util.Scanner;

public class MatrixSum {
    public static void main() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите кол-во строк в матрице:");
        int n = scanner.nextInt();
        System.out.println("Введите кол-во столбцов в матрице:");
        int m = scanner.nextInt();
        System.out.println("Введите матрицу: ");
        int[][] Matrix = new int[n][m];

        int sum = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                Matrix[i][j] = scanner.nextInt();
                sum += Matrix[i][j];
            }
        }

        System.out.println("Сумма матрицы: " + sum);
    }
}

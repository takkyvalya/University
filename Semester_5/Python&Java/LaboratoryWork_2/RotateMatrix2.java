//8. Задача: Повернуть двумерный массив на 90 градусов против часовой стрелке.
//Условие: Напишите метод, который принимает двумерный массив и возвращает новый массив,
//полученный путем поворота исходного массива на 90 градусов против часовой стрелке.

import java.util.Scanner;

public class RotateMatrix2 {
    public static void main() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите кол-во строк в матрице:");
        int n = scanner.nextInt();
        System.out.println("Введите кол-во столбцов в матрице:");
        int m = scanner.nextInt();
        System.out.println("Введите матрицу: ");
        int [][] Matrix = new int[n][m];
        for (int i = 0; i < n;  i++){
            for (int j = 0; j < m; j++){
                Matrix[i][j] = scanner.nextInt();
            }
        }

        int[][] RotatedMatrix = new int[m][n];

        // Поворот матрицы на 90 градусов по часовой стрелке
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                RotatedMatrix[m - 1 - j][i] = Matrix[i][j];
            }
        }

        //Вывод
        System.out.println("Повернутая матрица: ");
        for (int i = 0; i < m;  i++){
            for (int j = 0; j < n; j++){
                System.out.print(RotatedMatrix[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
}

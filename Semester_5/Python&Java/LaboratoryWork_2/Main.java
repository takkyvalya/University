import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println(
                "Выберите задачу (введите соответствующее число): \n" +
                "1. Найти наибольшую подстроку без повторяющихся символов. \n" +
                "2. Объединить два отсортированных массива \n" +
                "3. Найти максимальную сумму подмассива \n" +
                "4. Повернуть массив на 90 градусов по часовой стрелке \n" +
                "5. Найти пару элементов в массиве, сумма которых равна заданному числу \n" +
                "6. Найти сумму всех элементов в двумерном массиве \n" +
                "7. Найти максимальный элемент в каждой строке двумерного массива \n" +
                "8. Повернуть двумерный массив на 90 градусов против часовой стрелке \n"
        );
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        switch (n){
            case 1:
                Substring.main();
                break;
            case 2:
                Union.main();
                break;
            case 3:
                MaxSum.main();
                break;
            case 4:
                RotateMatrix.main();
                break;
            case 5:
                PairOfElements.main();
                break;
            case 6:
                MatrixSum.main();
                break;
            case 7:
                RowsMaximum.main();
                break;
            case 8:
                RotateMatrix2.main();
                break;
        }
    }
}

//auofjawoifhq3ouf

//4 -3 5 -9 -21 7 18 -3 21

//1 2 3
//4 5 6
//7 8 9
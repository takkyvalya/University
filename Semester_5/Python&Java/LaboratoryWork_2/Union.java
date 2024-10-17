import java.util.Arrays;
import java.util.Scanner;

//2. Задача: Объединить два отсортированных массива.
//Условие: Напишите метод, который принимает два отсортированных массива и возвращает
//новый массив, содержащий все элементы из обоих массивов в отсортированном порядке.

public class Union {
    public static void main() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите размер первого массива :");
        int n = scanner.nextInt();
        int [] FirstMassive = new int[n];
        System.out.println("Введите первый отсортированный массив длиной " + n + " :");
        for (int i=0; i< n; i++){
            FirstMassive[i] = scanner.nextInt();
        }
        Arrays.sort(FirstMassive); //на всякий случай еще раз отсортируем

        System.out.println("Введите размер второго массива :");
        int m = scanner.nextInt();
        int [] SecondMassive = new int[m];
        System.out.println("Введите второй отсортированный массив длиной " + m + " :");
        for (int i =0; i<m; i++){
            SecondMassive[i] = scanner.nextInt();
        }
        Arrays.sort(SecondMassive); //на всякий случай еще раз отсортируем

        int[] result = new int[n+m];

        int i =0, j=0;
        for(int k = 0; k < n + m; k++){
            if(i < n & j < m) {
                result[k] = (FirstMassive[i] <= SecondMassive[j]) ? FirstMassive[i++] : SecondMassive[j++];
            } else if (i < n) {
                result[k] = FirstMassive[i++];
            } else if (j < m) {
                result[k] = SecondMassive[j++];
            } else {
                System.out.println("ERORR!");
            }
        }

        //Вывод
        System.out.print("Result: ");
        for (int el : result){
            System.out.print(el + " ");
        }
        System.out.println();

    }
}

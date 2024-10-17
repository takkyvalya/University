//5. Задача: Найти пару элементов в массиве, сумма которых равна заданному числу.
//Условие: Напишите метод, который принимает массив целых чисел и целое число target и
//возвращает пару элементов массива, сумма которых равна target. Если такая пара не существует,
//метод должен вернуть null.

import java.util.ArrayList;
import java.util.Scanner;

public class PairOfElements {
    public static void main() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите целое число target:");
        int target = scanner.nextInt();
        System.out.println("Введите размер массива:");
        int n = scanner.nextInt();
        System.out.println("Введите элементы массива:");
        ArrayList<Integer> array = new ArrayList<>();
        for(int i = 0; i< n; i++){ array.add(scanner.nextInt());}

        boolean flag = false;
        //Будем для каждого элемента искать его пару
        int num = 0;
        for(int i = 0; i < n/2 + 1; i++){
            num = target - array.get(i);
            if(array.contains(num) == true)
            {
                flag = true; break;
            }
        }

        if(flag == true){
            System.out.println((target - num) + " " + num);
        } else {
            System.out.println("NULL");
        }
    }
}

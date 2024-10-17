//3. Задача: Найти максимальную сумму подмассива.
//Условие: Напишите метод, который принимает массив целых чисел и возвращает максимальную
//сумму подмассива (последовательных элементов).

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Scanner;

public class MaxSum {
    public static void main() {
        System.out.println("Введите размер массива:");
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println("Введите элементы массива:");
        int [] array = new int[n];
        for(int i = 0; i< n; i++){ array[i] = scanner.nextInt();}

        int CurrentSum = 0, MaxSum  = 0;
        ArrayList<Integer> Subarray = new ArrayList<>(); //Подмассивы, которые буду рассматривать
        ArrayList<Integer> MaxSubarray = new ArrayList<>(); //Максимальны подмассив
        //Рассмотрим всевозможные подмассивы и найдем с максимальной суммой
        for(int i = 0; i < n; i++) {
            Subarray.clear();
            CurrentSum = array[i];
            Subarray.add(array[i]);
            for(int j = i + 1; j < n; j++){
                CurrentSum += array[j];
                Subarray.add(array[j]);
                if(CurrentSum > MaxSum){
                    MaxSum = CurrentSum;
                    MaxSubarray = (ArrayList<Integer>) Subarray.clone();
                }
            }
        }

        //Вывод
        System.out.print("Подмассив: ");
        for(Object i:MaxSubarray){
            System.out.print(i + " ");
        }
        System.out.println();
        System.out.println("Сумма подмассива:" + MaxSum);
    }
}

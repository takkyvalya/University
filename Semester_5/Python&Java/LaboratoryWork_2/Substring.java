import java.util.ArrayList;
import java.util.Scanner;

//1. Задача: Найти наибольшую подстроку без повторяющихся символов.
//Условие: Напишите метод, который принимает строку и возвращает наибольшую подстроку, в
//которой все символы уникальны.

public class Substring {
    public static void main() {
        System.out.println("Введите строку:");
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();

        ArrayList<Character> charList = new ArrayList<>();

        for (char ch : s.toCharArray()) {
            charList.add(ch);  // добавляем каждый символ в ArrayList
        }

        int MaxLength = 0;
        int CurrentLength = 0;
        String result = "";
        ArrayList<Character> substring = new ArrayList<>(); //substring - это подстрочки, которые мы получаем пока ищем нужную

        for (char ch: charList){
            //проходимся по каждому символу и проверяем нет ли его уже в нашей подстроке
            if(substring.contains(ch)==false){
                CurrentLength++;
                substring.add(ch);
            } else {
                //если получившиеся подстрока наибольшая, то перезаписываем результат
                if (CurrentLength > MaxLength) {
                    MaxLength = CurrentLength;
                    result = "";
                    for(char a:substring)
                        result +=a;
                }
                //удаляем все символы из подстроки до повторющегося символа
                while (substring.get(0) != ch) {
                    substring.remove(0);
                    CurrentLength--;
                }
                substring.remove(0);
                substring.add(ch); //теперь у нас новая подстрока, которую мы будем увеличивать
            }
        }

        //Вывод
        System.out.print("Result: " + result);
        System.out.println();
    }
}


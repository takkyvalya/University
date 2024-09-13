import java.util.Scanner;

public class DoubleEven {
    public static void main() {
        System.out.print("Введите трехзначное число: ");
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();

        // Разобьем на циферки
        int digit1 = number / 100;
        int digit2 = (number / 10) % 10;
        int digit3 = number % 10;

        int sum = digit1 + digit2 + digit3;
        int product = digit1 * digit2 * digit3;

        // Проверка, что сумма и произведение четные
        if (sum % 2 == 0 && product % 2 == 0) {
            System.out.println("Число является дважды четным.");
        } else {
            System.out.println("Число НЕ является дважды четным.");
        }

        scanner.close();
    }
}

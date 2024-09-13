import java.util.Scanner;


public class Main {
    public static int Step(int n){ //вспомогательная функция для Collatz
        if (n%2==0){
            return n/2;
        } else {
            return 3*n+1;
        }
    }
    /////Сиракузская последовательность/////
    public static void Collatz(){
        System.out.print("Введите число n:");
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int count = 0; //количество шагов
        n = Step(n); //Делаем шаг вначале дабы избежать ошибки если n=1
        count++;
        while (n!=1){
            n = Step(n);
            count++;
        }
        System.out.println("Количество шагов: " + count);

        scanner.close();
    }

    /////Сумма ряда//////
    public static void SumOfSeries(){
        System.out.print("Введите число n:");
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] Series = new int[n]; //Массив для ряда чтобы вывсети его в конце в виде суммы
        for(int i =0; i<n;i++){
            Series[i] = scanner.nextInt();
        }
        int sum = 0;
        for(int i =0; i<n;i++){
            //sum += Math.pow(-1,i) * Series[i];
            //Хочу красиво вывсети ряд, поэтому реализую через if
            if(i%2==0 && i!=0){
                sum += Series[i];
                System.out.print(" + " + Series[i]);
            } else if (i!=0){
                sum -= Series[i];
                System.out.print(" - " + Series[i]);
            } else {
                sum += Series[i];
                System.out.print(Series[i]);
            }
        }
        System.out.print(" = " + sum); //Тут уже просто результат вывожу

        scanner.close();
    }

    ////Ищем Сокровища!////
    public static void TreasureHunt() {
        System.out.println("Введите координаты и указания:");
        Scanner scanner = new Scanner(System.in);
        int X = scanner.nextInt(); //Координаты клада
        int Y = scanner.nextInt();
        int currentX = 0; //Наши координаты
        int currentY = 0;
        int stepsCount = 0; // Счётчик указаний
        scanner.nextLine();

        // Читаем карту
        while (true) {
            String direction = scanner.nextLine().trim(); //напрваление
            if (direction.equals("стоп")) { break; }
            int distance = Integer.parseInt(scanner.nextLine().trim()); //расстояние
            switch (direction) {
                case "север":
                    currentY += distance;
                    break;
                case "юг":
                    currentY -= distance;
                    break;
                case "восток":
                    currentX += distance;
                    break;
                case "запад":
                    currentX -= distance;
                    break;
            }
            stepsCount++;

            // Мы нашли клад?
            if (currentX == X && currentY == Y) {
                break;
            }
        }
        System.out.println();
        System.out.println("Минимальное количество указаний: " + stepsCount);

        scanner.close();
    }

    /////Логистический максимин/////
    public static void Logist(){
        System.out.println("Введите данные: ");
        Scanner scanner = new Scanner(System.in);
        int NumberOfRoads = scanner.nextInt();
        int [][] tunnels = new int[NumberOfRoads][];

        //Заполним массив tunnels данными о высоте каждого туннеля
        for(int i = 0; i < NumberOfRoads; i++){
            int NumberOfTunnels = scanner.nextInt();
            tunnels[i] = new int[NumberOfTunnels];
            for(int j = 0; j < NumberOfTunnels; j++){
                tunnels[i][j] = scanner.nextInt();
            }
        }

        //Теперь найдем самый высокий туннель из туннелей с минимальной высотой на дороге
        int MaxOfMin = 0;
        int Road = 0;
        for (int i = 0; i < NumberOfRoads; i++){
            int MinOnRoad = 100000;
            for (int j = 0; j < tunnels[i].length; j++){
                MinOnRoad = Math.min(tunnels[i][j],MinOnRoad);
            }
            if(MinOnRoad > MaxOfMin){
                MaxOfMin = MinOnRoad;
                Road = i + 1;
            }
        }
        System.out.println();
        System.out.println("Номер дороги: " + Road);
        System.out.println("Наибольшая высота грузовика: " + MaxOfMin);

        scanner.close();
    }

    public static void main(String[] args) {
        System.out.println("Выберите задачу (введите соответствующее число): \n" +
                "1. Сиракузская последовательность \n" +
                "2. Сумма ряда \n" +
                "3. Ищем клад \n" +
                "4. Логистический максимин \n" +
                "5. Дважды четное число \n");
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        switch (n){
            case 1:
                Collatz();
                break;
            case 2:
                SumOfSeries();
                break;
            case 3:
                TreasureHunt();
                break;
            case 4:
                Logist();
                break;
            case 5:
                DoubleEven.main();
                break;
        }
    }
}


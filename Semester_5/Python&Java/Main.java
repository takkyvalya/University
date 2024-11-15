import Figures.Pawn;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {

        Board board = new Board();
        board.init();
        board.setColorGame('w');

        System.setOut(new PrintStream(System.out, true, StandardCharsets.UTF_8));

        System.out.println();

        boolean isGame = true;
        Scanner in = new Scanner(System.in);


        while (isGame){
            board.print_board();
            System.out.println();

            System.out.println("Управление:");
            System.out.println("----row col row1 col1: Ход фигуры из кретки (row, col) в (row1, col1)");

            switch (board.getColorGame()){
                case 'w': System.out.println("Ход белых"); break;
                case 'b': System.out.println("Ход черных"); break;
            }

            switch (board.GetCheck()){
                case 'w': System.out.println("Шах белым!!!"); break;
                case 'b': System.out.println("Шах черным!!!"); break;
            }
            switch (board.GetMate()){
                case 'w': System.out.println("Мат белым!!!"); break;
                case 'b': System.out.println("Мат черным!!!"); break;
            }

            System.out.print("Введите ход: ");

            String inputLine = in.nextLine();
            int row, col, row1, col1;
            String [] coords = inputLine.split(" ");
            row = Integer.parseInt(coords[0]);
            col = Integer.parseInt(coords[1]);
            row1 = Integer.parseInt(coords[2]);
            col1 = Integer.parseInt(coords[3]);

            while (!board.Move(row, col, row1, col1)){
                if(board.GetMate() != ' ') break;
                System.out.println("Ошибка! Повторите ход фигуры!");
                System.out.print("Введите ход: ");
                inputLine = in.nextLine();
                coords = inputLine.split(" ");
                row = Integer.parseInt(coords[0]);
                col = Integer.parseInt(coords[1]);
                row1 = Integer.parseInt(coords[2]);
                col1 = Integer.parseInt(coords[3]);
            }

            switch (board.getColorGame()){
                case 'w': board.setColorGame('b');break;
                case 'b': board.setColorGame('w');break;
            }
        }
        //test

    }
}
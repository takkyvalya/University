import Figures.*;

public class Board {

    private char colorGame;
    char Check = ' '; //шах
    char Mate = ' '; //мат

    public char GetCheck(){ return Check; }
    public char GetMate(){ return Mate; }

    public void setColorGame(char colorGame) {
        this.colorGame = colorGame;
    }

    public char getColorGame() {
        return colorGame;
    }


    private Figure fields[][] = new Figure[8][8];


    public void init() {
        this.fields[1] = new Figure[]{
                new Pawn("P", 'w'), new Pawn("P", 'w'), new Pawn("P", 'w'), new Pawn("P", 'w'),
                new Pawn("P", 'w'), new Pawn("P", 'w'), new Pawn("P", 'w'), new Pawn("P", 'w'),
        };
        this.fields[6] = new Figure[]{
                new Pawn("P", 'b'), new Pawn("P", 'b'), new Pawn("P", 'b'), new Pawn("P", 'b'),
                new Pawn("P", 'b'), new Pawn("P", 'b'), new Pawn("P", 'b'), new Pawn("P", 'b')
        };
        this.fields[0][0] = new Rook("R", 'w');
        this.fields[0][7] = new Rook("R", 'w');
        this.fields[7][0] = new Rook("R", 'b');
        this.fields[7][7] = new Rook("R", 'b');
        this.fields[0][1] = new Knight("N", 'w');
        this.fields[0][6] = new Knight("N", 'w');
        this.fields[7][1] = new Knight("N", 'b');
        this.fields[7][6] = new Knight("N", 'b');
        this.fields[0][2] = new Bishop("B", 'w');
        this.fields[0][5] = new Bishop("B", 'w');
        this.fields[7][2] = new Bishop("B", 'b');
        this.fields[7][5] = new Bishop("B", 'b');
        this.fields[0][4] = new King("K", 'w');
        this.fields[7][4] = new King("K", 'b');
        this.fields[0][3] = new Queen("Q", 'w');
        this.fields[7][3] = new Queen("Q", 'b');
        //this.fields[2][4] = new Pawn("P", 'w');
        //this.fields[4][4] = new King("K", 'b');

    }

    public String getCell(int row, int col) {
        Figure figure = this.fields[row][col];
        if (figure == null) {
            return "    ";
        }
        return " " + figure.getColor() + figure.getName() + " ";
    }

    public void print_board() {
        System.out.println(" +----+----+----+----+----+----+----+----+");
        for (int row = 7; row > -1; row--) {
            System.out.print(row);
            for (int col = 0; col < 8; col++) {
                System.out.print("|" + getCell(row, col));
            }
            System.out.println("|");
            System.out.println(" +----+----+----+----+----+----+----+----+");
        }

        for (int col = 0; col < 8; col++) {
            System.out.print("    " + col);
        }
    }

    // Найти позицию короля для указанного цвета
    private int[] findKingPosition(char color) {
        for (int row = 0; row < 8; row++) {
            for (int col = 0; col < 8; col++) {
                Figure figure = fields[row][col];
                if (figure instanceof King && figure.getColor() == color) {
                    return new int[]{row, col};
                }
            }
        }
        return null; // Король не найден
    }

    // Проверка на шахом
    public char isKingInCheck(char color) {
        int[] kingPos = findKingPosition(color);
        if (kingPos == null) return ' ';

        int kingRow = kingPos[0];
        int kingCol = kingPos[1];

        //System.out.println("Фаза 2");

        // Проверка угрозы от всех фигур противника
        for (int row = 0; row < 8; row++) {
            for (int col = 0; col < 8; col++) {
                Figure figure = fields[row][col];
                if (figure != null && figure.getColor() != color) {
                    if (figure.canAttack(row, col, kingRow, kingCol)) {
                        //System.out.println("Фаза 3 " + kingRow + " " + kingCol + "attack " + row + " " +  col);
                        return color; // Король под шахом
                    }
                }
            }
        }
        return ' '; // Шаха нет
    }

    // Проверка на мат
    public char isKingInCheckmate(char color) {
        // Проверяем, есть ли шах
        if (isKingInCheck(color) == ' ') {
            return ' '; // Если шаха нет, то и мата быть не может
        }

        // Проходим по всем клеткам доски
        for (int row = 0; row < 8; row++) {
            for (int col = 0; col < 8; col++) {
                Figure figure = fields[row][col];
                // Если на клетке стоит фигура текущего игрока
                if (figure != null && figure.getColor() == color) {
                    // Проверяем все возможные ходы фигуры
                    for (int row1 = 0; row1 < 8; row1++) {
                        for (int col1 = 0; col1 < 8; col1++) {
                            if (figure.canMove(row, col, row1, col1) || figure.canAttack(row, col, row1, col1)) {
                                // Выполняем временный ход
                                Figure temp = fields[row1][col1];
                                fields[row1][col1] = figure;
                                fields[row][col] = null;

                                // Проверяем, остался ли шах после хода
                                boolean stillInCheck = isKingInCheck(color) != ' ';

                                // Откатываем ход
                                fields[row][col] = figure;
                                fields[row1][col1] = temp;

                                // Если после хода шаха нет, то это не мат
                                if (!stillInCheck) {
                                    return ' ';
                                }
                            }
                        }
                    }
                }
            }
        }
        // Если ни один ход не устраняет шах, это мат
        return color;
    }



    public boolean move_figure(int row, int col, int row1, int col1) {
        Figure figure = this.fields[row][col];
        if (figure != null && figure.canMove(row, col, row1, col1) && this.fields[row1][col1] == null && figure.getColor() == this.colorGame) {
            this.fields[row1][col1] = figure;
            this.fields[row][col] = null;
            //Делаем проверку на шах и мат после каждого хода
            Check = colorGame == 'w' ? isKingInCheck('b') : isKingInCheck('w');
            Check = colorGame == 'w' ? isKingInCheckmate('b') : isKingInCheckmate('w');
            return true;
        } else if (figure.canAttack(row, col, row1, col1) && this.fields[row1][col1] != null && !this.fields[row1][col1].getName().equals("K") &&
                this.fields[row1][col1].getColor() != figure.getColor() && figure.getColor() == this.colorGame) {
            this.fields[row1][col1] = figure;
            this.fields[row][col] = null;
            //Делаем проверку на шах и мат после каждого хода
            Check = colorGame == 'w' ? isKingInCheck('b') : isKingInCheck('w');
            Check = colorGame == 'w' ? isKingInCheckmate('b') : isKingInCheckmate('w');
            return true;
        }
        return false;
    }

    public boolean Move(int row, int col, int row1, int col1) {
        Figure figure = this.fields[row][col];
        Figure otherFigure = this.fields[row1][col1];
        if(Mate != ' ') return false;
        if(Check != ' '){ //Если шах, то делаем проверку будет ли шах после хода
            System.out.println(this.fields[row][col]);
            //System.out.println("Фаза 1 " + this.fields[row][col].getName());
            this.fields[row1][col1] = figure;
            this.fields[row][col] = null;
            if(isKingInCheck(colorGame) == ' ') {
                this.fields[row1][col1] = otherFigure;
                this.fields[row][col] = figure;
                return move_figure(row, col, row1, col1);
            } else {
                this.fields[row1][col1] = otherFigure;
                this.fields[row][col] = figure;
                return false;
            }
        } else { //Если шаха нет, ходим как обычно
            return move_figure(row, col, row1, col1);
        }
    }
}

package Figures;

public class King extends Figure {
    public King(String name, char color) {
        super(name, color);
    }

    @Override
    public boolean canMove(int row, int col, int row1, int col1) {

        return  (row>= 0 && row < 8) && (col>=0 && col<8) &&
                (row1>= 0 && row1 < 8) && (col1>=0 && col1<8) &&
                ((col!=col1) || (row!=row1)) &&
                (Math.abs(col-col1)<=1) && (Math.abs(row-row1)<=1);
    }

    @Override
    public boolean canAttack(int row, int col, int row1, int col1) {
        return canMove(row,col,row1,col1);
    }
}

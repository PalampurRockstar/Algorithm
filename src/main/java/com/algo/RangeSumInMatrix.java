package com.algo;

public class RangeSumInMatrix {
    int sumMatrix[][];

    RangeSumInMatrix(int mat[][]) {
        if (mat.length > 0 && mat[0].length > 0)
            calculateSumMat(mat);
        printSumMat();
    }

    private void printSumMat() {
        for (int i = 0; i < sumMatrix.length; ++i) {
            for (int j = 0; j < sumMatrix[0].length; ++j)
                System.out.print(sumMatrix[i][j] + " ");
            System.out.println();
        }
    }

    private void calculateSumMat(int[][] mat) {
        sumMatrix = new int[mat.length + 1][mat[0].length + 1];

        for (int i = 1; i < sumMatrix.length; ++i) {
            for (int j = 1; j < sumMatrix[0].length; ++j) {
                sumMatrix[i][j] = sumMatrix[i][j - 1] + mat[i - 1][j - 1] + sumMatrix[i - 1][j] - sumMatrix[i - 1][j - 1];
            }
        }
    }

    public static void main(String[] args) {
        int matrix[][] = new int[][]{
                {3, 0, 1, 4, 2},
                {5, 6, 3, 2, 1},
                {1, 2, 0, 1, 5},
                {4, 1, 0, 1, 7}
        };
        RangeSumInMatrix calculator = new RangeSumInMatrix(matrix);
        int sum = calculator.calculateRangeSum(2, 3, 3, 4);
        System.out.println("sum: " + sum);

    }

    private int calculateRangeSum(int x1, int y1, int x2, int y2) {
        int topLeftx = x1;
        int topLefty = y1;
        System.out.println("topRight : " + sumMatrix[topLeftx][topLefty]);

        int topRightx = x1;
        int topRighty = y2 + 1;
        System.out.println("topRight : " + sumMatrix[topRightx][topRighty]);

        int bottomLeftx = x2 + 1;
        int bottomLefty = y1;
        System.out.println("bottomLeft : " + sumMatrix[bottomLeftx][bottomLefty]);

        int bottomRightx = x2 + 1;
        int bottomRighty = y2 + 1;
        System.out.println("bottomRight : " + sumMatrix[bottomRightx][bottomRighty]);

        return sumMatrix[bottomRightx][bottomRighty] - (sumMatrix[bottomLeftx][bottomLefty] + sumMatrix[topRightx][topRighty])+sumMatrix[topLeftx][topLefty];
    }
}

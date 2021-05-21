package com.algo;

public class MatrixMultiply {
    public static void main(String[] args) {

        int matrix1[][] = new int[][]{
                {1, 2, 3},
                {6, 8, 2}
        };
        int matrix2[][] = new int[][]{
                {1, 2, 3, 1},
                {6, 8, 2, 2},
                {9, 8, 5, 4}
        };
        int out[][] = multiply(matrix1, matrix2);
        printMatrix(matrix1);
        printMatrix(matrix2);
        System.out.println("-----");
        printMatrix(out);


    }

    static void printMatrix(int matrix[][]) {
        for (int i = 0; i < matrix.length; ++i) {
            for (int j = 0; j < matrix[0].length; ++j) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }

    private static int[][] multiply(int[][] matrix1, int[][] matrix2) {
        if (matrix1.length > 0 && matrix2.length > 0) {
            int m1c = matrix1[0].length;
            int m2r = matrix2.length;
            if (m1c == m2r) {
                int m1r = matrix1.length;
                int m2c = matrix2[0].length;
                int count = 0;
                int result[][] = new int[m1r][m2c];
                for (int i = 0; i < m1r; ++i)
                    for (int j = 0; j < m2c; ++j)
                        for (int k = 0; k < m1c; ++k)
                            result[i][j] += matrix1[i][k] * matrix2[k][j];
                return result;
            }
        }
        return null;
    }
}

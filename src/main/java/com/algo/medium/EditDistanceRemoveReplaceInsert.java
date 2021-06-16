package com.algo.medium;

public class EditDistanceRemoveReplaceInsert {

    /*key points:
    1. compare with rest("") string directly gives other string length as result
    2. if equal reduce both and no increment in count
    3. if not equal try 3 possibilities (remove,insert & replace) +1(cost of move)
    4. back track to find elements
    */

    public static void main(String[] args) {
        String input1 = "horse", input2 = "ros";
        int resultRecursively = findByRecursively(input1, input2);
        System.out.println("resultRecursively: " + resultRecursively);

        String resultTabulation = findByTabulation(input1, input2);
        System.out.println("resultTabulation: " + resultTabulation);
    }

    private static String findByTabulation(String input1, String input2) {
        int mat[][] = new int[input1.length() + 1][input2.length() + 1];

        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[0].length; ++j) {
                if (i == 0) {
                    mat[i][j] = j;
                } else if (j == 0) {
                    mat[i][j] = i;
                } else if (input1.charAt(i - 1) == input2.charAt(j - 1)) {
                    mat[i][j] = mat[i - 1][j - 1];
                } else {
                    mat[i][j] = min(mat[i - 1][j],//remove
                            mat[i][j - 1],//insert
                            mat[i - 1][j - 1]) + 1; //replace
                }
            }
        }
        //back track
        StringBuilder result = new StringBuilder();
        for (int i = mat.length - 1, j = mat[0].length - 1; i > 0 && j > 0; ) {
            if (input1.charAt(i - 1) == input2.charAt(j - 1)) {
                i--;
                j--;
            } else {
                result.append(input1.charAt(i - 1));
                int min = min(mat[i][j - 1], mat[i - 1][j], mat[i - 1][j - 1]);
                if (min == mat[i][j - 1]) {
                    j--;
                } else if (min == mat[i - 1][j]) {
                    i--;
                } else {
                    j--;
                    i--;
                }
            }
        }
        return result.toString();
    }

    private static int findByRecursively(String input1, String input2) {
        if (input1.length() == 0) return input2.length();
        if (input2.length() == 0) return input1.length();

        if (input1.charAt(0) == input2.charAt(0))
            return findByRecursively(input1.substring(1), input2.substring(1));
        else {
            int remove = findByRecursively(input1.substring(1), input2);
            int replace = findByRecursively(input1.substring(1), input2.substring(1));
            int insert = findByRecursively(input1, input2.substring(1));
            return min(remove, replace, insert) + 1;
        }
    }

    static int min(int a, int b, int c) {
        return Integer.min(a, Integer.min(b, c));
    }
}

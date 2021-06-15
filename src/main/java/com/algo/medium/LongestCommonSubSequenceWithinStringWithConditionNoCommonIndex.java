package com.algo.medium;

import io.vavr.control.Try;

public class LongestCommonSubSequenceWithinStringWithConditionNoCommonIndex {
    /*
    find LCSS within its string
    without having the same index
    */
    public static void main(String[] args) {
        String input = "apqadpcdq";
        String resultTabulation = findByTabulation(input);
        System.out.println("resultTabulation : " + resultTabulation);

        String resultRecursion = findByRecursion(input, input.length() - 1, input, input.length() - 1);
        System.out.println("resultRecursion : " + resultRecursion);
    }

    private static String findByRecursion(String input1, int l1, String input2, int l2) {
        if (input1.length() == 0 || input2.length() == 0) return new String();
        if (l1 != l2 && input1.charAt(l1) == input2.charAt(l2)) {
            String result = findByRecursion(
                    input1.substring(0, input1.length() - 1),
                    l1 - 1,
                    input2.substring(0, input2.length() - 1),
                    l2 - 1);
            return input1.charAt(l1) + result;
        } else {
            String right = findByRecursion(input1.substring(0, input1.length() - 1), l1 - 1, input2, l2);
            String left = findByRecursion(input1, l1, input2.substring(0, input2.length() - 1), l2 - 1);
            return (left.length() > right.length() ? left : right);
        }
    }

    private static String findByTabulation(String input) {
        int mat[][] = new int[input.length() + 1][input.length() + 1];
        for (int i = 0; i < mat.length; ++i)
            for (int j = 0; j < mat[0].length; ++j)
                if (j >= i)
                    if (i == 0 || j == 0)
                        continue;
                    else if (input.charAt(i - 1) == input.charAt(j - 1) && i != j)
                        mat[i][j] = mat[i - 1][j - 1] + 1;
                    else
                        mat[i][j] = Integer.max(mat[i][j - 1], mat[i - 1][j]);
        //back track
        StringBuilder result = new StringBuilder();
        if (mat[mat.length - 1][mat[0].length - 1] != 0)
            for (int i = mat.length - 1, j = mat[0].length - 1; i > 0 && i > 0; ) {
                if (input.charAt(i - 1) == input.charAt(j - 1) && i != j) {
                    result.append(input.charAt(i - 1));
                    i--;
                    j--;
                } else if (mat[i - 1][j] > mat[i][j - 1])
                    i--;
                else
                    j--;
            }
        return result.toString();
    }
}

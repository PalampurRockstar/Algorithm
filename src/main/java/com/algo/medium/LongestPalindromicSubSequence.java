package com.algo.medium;

import java.util.HashMap;
import java.util.Map;

public class LongestPalindromicSubSequence {
    public static void main(String[] args) {
        Map<String, String> solved = new HashMap<>();
        String input = "abkssccba";
        String topDownResult = topDownRecursionMemorization(input, solved);
        System.out.println("Result : " + topDownResult);
        String bottomUp = bottomUpTabulation(input);
        System.out.println("Result : " + bottomUp);
    }

    private static String bottomUpTabulation(String input) {
        int len = input.length();
        int mat[][] = new int[len][len];
        for (int i = 0; i < len; ++i) {
            for (int j = 0; j < len - i; ++j) {
                int k = j + i;
                if (i == 0)
                    mat[j][k] = 1;
                else if (i == 1)
                    mat[j][k] = input.charAt(j) == input.charAt(k) ? 2 : 1;
                else {
                    if (input.charAt(j) == input.charAt(k)) {
                        mat[j][k] = mat[j + 1][k - 1] + 2;
                    } else {
                        mat[j][k] = Integer.max(mat[j + 1][k], mat[j][k - 1]);
                    }
                }
            }
        }
        //back track
        char result[] = new char[mat[0][len - 1]];
        int rBack = 0, rFront = result.length - 1;
        for (int front = len - 1, back = 0; back <= front; ) {
            if (input.charAt(back) == input.charAt(front)) {
                result[rBack++] = input.charAt(back++);
                result[rFront--] = input.charAt(front--);
            } else {
                if (mat[front][back + 1] < mat[front - 1][back]) {
                    front--;
                } else {
                    back++;
                }
            }
        }
        return new String(result);
    }

    static void print(int mat[][]) {
        System.out.println("----------------------------");
        for (int i = 0; i < mat.length; ++i) {
            for (int j = 0; j < mat[0].length; ++j) {
                System.out.print(mat[i][j] + "\t");
            }
            System.out.println();
        }
        System.out.println("----------------------------");
    }

    private static String topDownRecursionMemorization(String input, Map<String, String> solved) {
        if (solved.containsKey(input))
            return solved.get(input);
        int len = input.length();
        if (len == 0 || len == 1) {
            solved.put(input, input);
            return input;
        }
        if (input.charAt(0) == input.charAt(len - 1)) {
            String mid = topDownRecursionMemorization(input.substring(1, len - 1), solved);
            solved.put(input, input.charAt(0) + mid + input.charAt(len - 1));
            return solved.get(input);
        } else {
            String left = topDownRecursionMemorization(input.substring(1, len), solved);
            String right = topDownRecursionMemorization(input.substring(0, len - 1), solved);
            solved.put(input, left.length() > right.length() ? left : right);
            return solved.get(input);
        }
    }

}

package com.algo.medium;

import java.util.HashMap;
import java.util.Map;

public class LongestCommonSubSequence {

    public static void main(String[] args) {
        String input2 = "abcd";
        String input1 = "aebd";

        String resultRecursively = findRecursively(input1, input2, new HashMap<>());
        System.out.println("resultRecursively : " + resultRecursively);

        String resultOptimal = findByAggressiveSolutionOptimalMost(input1, input2);
        System.out.println("resultOptimal : " + resultOptimal);

        String resultTabulation = findByTabulation(input1, input2);
        System.out.println("resultTabulation : " + resultTabulation);
    }

    static String findByTabulation(String input1, String input2) {
        int len1 = input1.length();
        int len2 = input2.length();
        int mat[][] = new int[len1 + 1][len2 + 1];
        StringBuilder result = new StringBuilder();
        for (int i = len1; i >= 0; --i) {
            for (int j = len2; j >= 0; --j) {
                if (i == len1 || j == len2) {
                    mat[i][j] = 0;
                } else if (input1.charAt(i) == input2.charAt(j)) {
                    mat[i][j] = mat[i + 1][j + 1] + 1;
                    result.append(input1.charAt(i));
                } else {
                    mat[i][j] = Integer.max(mat[i + 1][j], mat[i][j + 1]);
                }
            }
        }
        System.out.println("Len : " + mat[0][0]);
        return result.reverse().toString();
    }

    private static String findByAggressiveSolutionOptimalMost(String input1, String input2) {
        StringBuilder result = new StringBuilder();
        int i = 0, j = 0;
        boolean traverseI = false;
        while (i < input1.length() || j < input2.length()) {
            if (traverseI) {
                int foundIndex = findLinear(i, input1, input2.charAt(j));
                if (foundIndex != -1) {
                    result.append(input2.charAt(j));
                    i = foundIndex + 1;
                }
                j++;
                traverseI = false;
            } else {
                int foundIndex = findLinear(j, input2, input1.charAt(i));
                if (foundIndex != -1) {
                    result.append(input1.charAt(i));
                    j = foundIndex + 1;
                }
                i++;
                traverseI = true;
            }
        }
        return result.toString();
    }

    static int findLinear(int start, String input, char toFind) {
        for (int k = start; k < input.length(); ++k) {
            if (toFind == input.charAt(k)) {
                return k;
            }
        }
        return -1;
    }

    private static String findRecursively(String input1, String input2, Map<String, String> qa) {
        if (qa.containsKey(input1 + input2)) return qa.get(input1 + input2);
        if (input1.length() == 0 || input2.length() == 0) {
            qa.put(input1 + input2, new String());
            return qa.get(input1 + input2);
        }
        if (input1.length() == 1 && input2.length() == 1) {
            qa.put(input1 + input2, String.valueOf(input1.charAt(0) == input2.charAt(0) ? input1.charAt(0) : ""));
            return qa.get(input1 + input2);
        }
        if (input1.charAt(0) == input2.charAt(0)) {
            qa.put(input1 + input2, input1.charAt(0) + findRecursively(input1.substring(1), input2.substring(1), qa));
            return qa.get(input1 + input2);
        } else {
            String right = findRecursively(input1.substring(1), input2, qa);
            String left = findRecursively(input1, input2.substring(1), qa);
            qa.put(input1 + input2, right.length() < left.length() ? left : right);
            return qa.get(input1 + input2);
        }
    }

}

package com.algo.easy;

public class RunLengthEncoding {
    public static void main(String[] args) {
        String input = "wwwwaaadqexxxxxx";
        String result = getRunLengthEncodedString(input);
        System.out.println("Result: " + result);
        String resultByPartitioning = getRunLengthEncodedString(input);
        System.out.println("ResultByPartitioning: " + resultByPartitioning);
    }

    private static String getRunLengthEncodedString(String input) {
        if (input == null) return null;

        StringBuilder result = new StringBuilder();
        int eachCount = 0;
        for (int i = 0; i < input.length() - 2; i++) {
            if (input.charAt(i) == input.charAt(i + 1)) {
                result.append(input.charAt(i));
                eachCount++;
                for (int front = i + 1, back = i; front < input.length() && input.charAt(front) == input.charAt(back); front++) {
                    eachCount++;
                    i = front;
                }
                result.append(eachCount);
                eachCount = 0;
            } else {
                result.append(input.charAt(i));
                result.append(1);
            }
        }
        return result.toString();
    }

    private static String getRunLengthEncodedStringByPartitioning(String input) {
        if (input == null) return null;
        StringBuilder result = new StringBuilder();
        int eachCount = 0;
        for (int i = 0; i < input.length() - 2; i++) {
            if (input.charAt(i) == input.charAt(i + 1)) {
                eachCount++;
            } else {
                eachCount++;
                result.append(input.charAt(i));
                result.append(eachCount);
            }
        }
        return result.toString();
    }

}

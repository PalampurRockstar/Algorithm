package com.algo.medium;

public class LongestPalindromicSubString {
    public static void main(String[] args) {
        String input = "abaxabaxabb";
        final var arrayResult = topDownWithArray(input);
        System.out.println(arrayResult);
        final var recursiveSolution = topDownFindRecursively(input);
        System.out.println(recursiveSolution);
        final var forLoop = topDownWithForLoop(input);
        System.out.println(forLoop);
    }

    static String topDownFindRecursively(String input) {
        String max = "";
        for (int i = 0; i < input.length() - 1; ++i) {
            String two = checkRightLeft(input, i, i + 1);
            if (two != null && max.length() < two.length())
                max = two;
            String three = checkRightLeft(input, i, i + 2);
            if (three != null && max.length() < three.length())
                max = three;
        }
        return max;
    }

    private static String topDownWithForLoop(String input) {
        int maxLen = 0;
        int backIndex = 0;
        for (int i = 1; i < input.length(); ++i) {
            for (int back = i - 1, front = i; back >= 0 && front < input.length() && input.charAt(back) == input.charAt(front); ++front, --back) {
                int diff = front - back + 1;
                if (diff > maxLen) {
                    backIndex = back;
                    maxLen = diff;
                }
            }
            for (int back = i - 1, front = i + 1; back >= 0 && front < input.length() && input.charAt(back) == input.charAt(front); ++front, --back) {
                int diff = front - back + 1;
                if (diff > maxLen) {
                    backIndex = back;
                    maxLen = diff;
                }
            }
        }
        return maxLen != 0 ? input.substring(backIndex, backIndex + maxLen) : null;
    }

    private static String checkRightLeft(String input, int start, int end) {
        if (start >= 0 && end < input.length() && input.charAt(start) == input.charAt(end)) {
            String result = checkRightLeft(input, start - 1, end + 1);
            if (result != null) {
                return result;
            } else
                return input.substring(start, end + 1);
        } else
            return null;
    }

    private static String topDownWithArray(String input) {
        int len = input.length();
        if (len == 0) return "";
        int max = 0;
        int maxIndexX = 0;
        int maxIndexY = 0;
        for (int i = 0; i < (len * 2) - 3; ++i) {
            int index = (i % (len - 1));
            int gap = i < len - 1 ? 1 : 2;
            int x = index;
            int y = index + gap;
            for (int currentCount = 1, nextX = x, nextY = y; nextX < len && nextY > -1 && input.charAt(nextX) == input.charAt(nextY); ++nextX, --nextY, ++currentCount) {
                if (max < currentCount) {
                    max = currentCount;
                    maxIndexX = nextX;
                    maxIndexY = nextY;
                }
            }
        }
        return max != 0 ? input.substring(maxIndexY, maxIndexX + 1) : "";
    }
}

package com.algo;


public class RegexStarAndDot {


    public boolean matchRegexRecursion(String text, String pattern) {
        if (pattern.length() == 0) return text.length() == 0;
        if (pattern.length() > 1 && pattern.charAt(1) == '*') {
            boolean res = matchRegexRecursion(text, pattern.substring(2));
            if (text.length() > 0 && pattern.charAt(0) == text.charAt(0) || pattern.charAt(0) == '.') {
                res = res || matchRegexRecursion(text.substring(1), pattern);
            }
            return res;
        } else if (pattern.length() > 0 && (pattern.charAt(0) == text.charAt(0) || pattern.charAt(0) == '.')) {
            return matchRegexRecursion(text.substring(1), pattern.substring(1));
        } else
            return false;
    }

    public boolean matchRegex(String text, String pattern) {
        boolean possible[][] = new boolean[text.length() + 1][pattern.length() + 1];
        for (int i = 0; i < possible.length; ++i) {
            for (int j = 0; j < possible[0].length; ++j) {
                if (i == 0 && j == 0) {
                    possible[i][j] = true;
                } else if (i == 0) {
                    if (pattern.charAt(j - 1) == '*')
                        possible[i][j] = possible[i][j - 2];
                } else if (j == 0) {
                    possible[i][j] = false;
                } else {
                    char pChar = pattern.charAt(j - 1);
                    char tChar = text.charAt(i - 1);
                    if (pChar == '.' || pChar == tChar) {
                        possible[i][j] = possible[i - 1][j - 1];
                    } else if (pChar == '*') {
                        possible[i][j] = possible[i][j - 2];
                        if (tChar == pattern.charAt(j - 2) || pattern.charAt(j - 2) == '.') {
                            possible[i][j] = possible[i][j] || possible[i - 1][j];
                        }
                    }
                }
            }
        }
        return possible[text.length()][pattern.length()];
    }

    public static void main(String args[]) {
        RegexStarAndDot rm = new RegexStarAndDot();

        System.out.println(rm.matchRegex("sourabh", "sourabh") == true);
        System.out.println(rm.matchRegex("sourabh", "sourabh*a*b*") == true);
        System.out.println(rm.matchRegex("", "a*b*") == true);
        System.out.println(rm.matchRegexRecursion("abbbbccc", "a*ab*bbbbc*") == true);
        System.out.println(rm.matchRegex("abbbbccc", "aa*bbb*bbbc*") == false);
        System.out.println(rm.matchRegex("abbbbccc", ".*bcc") == false);
        System.out.println(rm.matchRegex("abbbbccc", ".*bcc*") == true);
        System.out.println(rm.matchRegex("abbbbccc", ".*bcc*") == true);
        System.out.println(rm.matchRegex("aaa", "ab*a*c*a") == true);
        System.out.println(rm.matchRegex("aa", "a*") == true);
    }
}

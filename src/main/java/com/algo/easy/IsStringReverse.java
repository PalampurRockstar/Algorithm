package com.algo.easy;

public class IsStringReverse {
    public static void main(String[] args) {

        final var result=reverseString("sourabh","hbaruos");
        System.out.println("Resiult : " +result);
    }

    public static boolean reverseString(String s1, String s2) {
        if (s1.length() != s2.length()) return false;
        if (s1.length() == 1 && s1.charAt(0) == s2.charAt(0)) return true;
        if (s1.charAt(0) == s2.charAt(s2.length() - 1)) {
            return reverseString(s1.substring(1), s2.substring(0, s2.length() - 1));
        }else
            return false;
    }
}

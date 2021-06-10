package com.algo.easy;

public class ReverseString {
    public static void main(String[] args) {
        final var rec = reverseRec("sourabh");
        final var linear = reverseLinear("sourabh");
        System.out.println("Recursion: " + rec);
        System.out.println("Linear: " + linear);
        System.out.println("Palindrome: nitin : " + isPalindrome("nitin"));
        System.out.println("Palindrome: sourabh : " + isPalindrome("sourabh"));
    }

    private static boolean isPalindrome(String input) {
        if(input!=null)
            return reverseLinear(input).equals(input);
        return false;
    }

    public static String reverseRec(String input) {
        int len = input.length();
        if (len == 1) return "" + input.charAt(0);
        return input.charAt(input.length() - 1) + reverseRec(input.substring(0, len - 1));
    }

    public static String reverseLinear(String input) {
        if (input != null && input.length() > 1) {
            char[] reversetList = new char[input.length()];
            for (int front = input.length() - 1, back = 0; front >= back; --front, ++back) {
                reversetList[back] = input.charAt(front);
                reversetList[front] = input.charAt(back);
            }
            return new String(reversetList);
        } else
            return input;
    }
}

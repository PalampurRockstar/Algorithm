package com.algo;

public class Reverse {

    public static void main(String[] args) {
        System.out.println(reverseInImmutability("Sourabhk"));
    }
    static String reverse(String str) {
        int front = str.length() - 1;
        int back = 0;
        final StringBuilder builder = new StringBuilder(str);
        while (back < front) {
            builder.setCharAt(back, str.charAt(front));
            builder.setCharAt(front, str.charAt(back));
            back++;
            front--;
        }
        return builder.toString();
    }

    static String reverseInImmutability(String str) {
        System.out.println(str.length());
        if (str.length() == 1)
            return String.valueOf(str.charAt(0));
        return new StringBuilder()
                .append(str.charAt(str.length() - 1))
                .append(reverseInImmutability(str.substring(0, str.length()-1 )))
                .toString();
    }
}

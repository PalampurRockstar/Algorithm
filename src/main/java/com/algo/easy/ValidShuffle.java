package com.algo.easy;

public class ValidShuffle {
    public static void main(String[] args) {
        System.out.println(checkShuffle("abc", "zhdy", "sourabh"));
        System.out.println(checkShuffle("abc", "zhdy", "zhabc"));
    }

    public static boolean checkShuffle(String first, String second, String result) {
        String input = first.concat(second);
        boolean exist[] = new boolean[26];
        for (int i = 0; i < input.length(); ++i)
            exist[input.charAt(i) - 'a'] = true;
        for (int i = 0; i < result.length(); ++i)
            if (!exist[result.charAt(i) - 'a'])
                return false;
        return true;
    }
}
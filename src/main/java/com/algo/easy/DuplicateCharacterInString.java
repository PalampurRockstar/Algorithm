package com.algo.easy;

public class DuplicateCharacterInString {
    public static void main(String[] args) {
        System.out.println(findDuplicateChar("sosurbabh"));
    }

    public static String findDuplicateChar(String input) {
        String lowerCase = input.toLowerCase();
        boolean visited[] = new boolean[26];
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < input.length(); ++i) {
            int index = lowerCase.charAt(i) - 'a';
            if (visited[index])//check whether visited
                sb.append(lowerCase.charAt(i));
            else
                visited[index] = true;//now visited
        }
        return sb.toString();
    }
}

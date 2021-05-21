package com.algo;

public class StringAnagramCount {

    public static void main(String[] args) {
        String str1 = "sourab";
        String str2 = "raghav";
        int count = isStringAnagram(str1, str2);
        System.out.println("count : " + count);
    }

    private static int isStringAnagram(String str1, String str2) {
        int freq[] = new int[26];
        for (int i = 0; i < str1.length(); ++i)
            freq[str1.charAt(i) - 'a']++;
        int count = 0;
        for (int i = 0; i < str2.length(); ++i) {
            freq[str2.charAt(i) - 'a']--;
            if (freq[str2.charAt(i) - 'a'] < 0)
                count++;
        }
        return count;
    }
}

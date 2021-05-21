package com.algo;

import java.util.HashMap;
import java.util.Map;

public class EditDistance {
    static Map<String, Integer> map = new HashMap<>();

    public static void main(String[] args) {
        findEditDistance("horse", "ros");
    }

    private static void findEditDistance(String str1, String str2) {
        System.out.println("recursively: " + recursively(str1, str2, str1.length(), str2.length()));
        System.out.println("editDistUsingArray: " + editDistUsingArray(str1, str2, str1.length(), str2.length()));
    }

    static int editDistUsingArray(String str1, String str2, int m, int n) {
        int dp[][] = new int[m + 1][n + 1];
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0)
                    dp[i][j] = j;
                else if (j == 0)
                    dp[i][j] = i;
                else if (str1.charAt(i - 1) == str2.charAt(j - 1))
                    dp[i][j] = dp[i - 1][j - 1];
                else
                    dp[i][j] = 1 + min(dp[i][j - 1], // Insert
                            dp[i - 1][j], // Remove
                            dp[i - 1][j - 1]); // Replace
            }
        }
        return dp[m][n];
    }

    private static int recursively(String s1, String s2, int s1l, int s2l) {
        if (s1l == 0) return s2l;
        if (s2l == 0) return s1l;
        String key = s1l + ":" + s2l;
        if (map.containsKey(key)) return map.get(key);
        else if (s1.charAt(s1l - 1) == s2.charAt(s2l - 1)) {
            map.put(key, recursively(s1, s2, s1l - 1, s2l - 1));
        } else {
            map.put(key, min(
                    recursively(s1, s2, s1l - 1, s2l - 1),
                    recursively(s1, s2, s1l - 1, s2l),
                    recursively(s1, s2, s1l, s2l - 1)) + 1);
        }
        return map.get(key);
    }

    static int min(int a, int b, int c) {
        return Math.min(a, Math.min(b, c));
    }
}


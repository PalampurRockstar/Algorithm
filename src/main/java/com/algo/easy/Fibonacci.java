package com.algo.easy;

import java.util.HashMap;
import java.util.Map;

public class Fibonacci {
    static Map<Integer, Integer> map = new HashMap<>();

    public static void main(String[] args) {
        int number = 16;
        int result = fibDp(10);
        System.out.println(result);
    }
    private static int fibDp(int n) {
        if (n == 0 || n == 1)
            return n;
        if (map.containsKey(n))
            return map.get(n);
        map.put(n, fibDp(n - 1) + fibDp(n - 2));
        return map.get(n);
    }
}

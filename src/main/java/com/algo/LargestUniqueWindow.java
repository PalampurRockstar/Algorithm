package com.algo;

import java.util.HashMap;
import java.util.Map;

public class LargestUniqueWindow {

    public static void main(String[] args) {
        int result = longestUniqueSubString("abbcdafeegh");
        System.out.println("result : " + result);
    }

    static int longestUniqueSubString(String list) {
        Map<Character, Integer> visited = new HashMap<>();
        int back = 0;
        int max = 0;
        for (int front = 0; front < list.length(); ++front) {
            if (visited.containsKey(list.charAt(front))) {
                back = visited.get(list.charAt(front)) + 1;
            }
            visited.put(list.charAt(front), front);
            if (max < (front - back)) {
                max = front - back;
                System.out.println(list.substring(back, front + 1));
            }
        }
        return max;
    }
}

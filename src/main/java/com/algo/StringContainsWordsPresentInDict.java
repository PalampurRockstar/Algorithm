package com.algo;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class StringContainsWordsPresentInDict {
    static Set<String> dict = new HashSet<>();
    static Map<String, Boolean> map = new HashMap<>();

    static {
        dict.add("cat");
        dict.add("category");
        dict.add("do");
        dict.add("dog");
    }

    public static void main(String[] args) {
        String input = "dogcategory";
        boolean result = sentenceContainsWordsInDict(input);
        System.out.println(result);
    }

    private static boolean sentenceContainsWordsInDict(String input) {
        if (dict.contains(input)) {
            map.put(input, true);
            return map.get(input);
        }
        if (map.containsKey(input))
            return map.get(input);
        for (int i = 0; i < input.length(); ++i) {
            if (dict.contains(input.substring(0, i + 1)) && sentenceContainsWordsInDict(input.substring(i + 1))) {
                map.put(input, true);
                return map.get(input);
            }
        }
        map.put(input, false);
        return map.get(input);
    }
}

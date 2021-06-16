package com.algo.easy;

import java.util.HashSet;
import java.util.Set;

public class AllPossibleSubSequence {
    public static void main(String[] args) {
        String input = "sou";
        System.out.println("-------RecUsingSet-------");
        findByRecUsingSet(input)
                .forEach(System.out::println);
        System.out.println("-------Tabulation-------");
        findByTabulation(input);
        System.out.println("-------Recursion-------");
        findByRec("", input);
    }

    static void findByTabulation(String input) {
        int len = input.length();
        for (int i = 1; i < Math.pow(2, len); ++i) {
            StringBuilder str = new StringBuilder();
            for (int j = 0; j < len; ++j) {
                if ((i & (1 << j)) != 0)//magical formulae  ((nthString & (1 << ithCharacter)) != 0) is equal to zero or not
                    str.append(input.charAt(j));
            }
            System.out.println(str.toString());
        }
    }

    static Set<String> findByRecUsingSet(String input) {
        Set<String> set = new HashSet();
        if (input == null || input.length() == 0) return set;
        if (input.length() == 1) {
            set.add(input);
            set.add("");
        }
        Set<String> restSet = findByRecUsingSet(input.substring(1));
        for (String each : restSet)
            set.add(input.substring(0, 1) + each);
        set.addAll(restSet);
        return set;
    }

    static void findByRec(String front, String rest) {
        if (rest == null || rest.length() == 0) return;
        if (rest.length() == 1) {
            System.out.println(front + rest);
            System.out.println(front);
        }
        findByRec(front + rest.substring(0, 1), rest.substring(1));
        findByRec(front, rest.substring(1));
    }
}

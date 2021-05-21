package com.algo;

import javax.imageio.stream.ImageInputStream;
import java.util.*;

public class StringCanBeConvertedToAnotherWithAnyOperation {
    static boolean check(String s1, String s2) {
        int n = s1.length();
        int m = s2.length();
        System.out.println(s1 + " : " + n);
        System.out.println(s2 + " : " + m);

//        Set<String> set = new HashSet<>();
        Set<String> set = new LinkedHashSet<>();
        set.add(0 + ":" + 0);

        for (int i = 0; i < s1.length(); i++) {
            for (int j = 0; j < s2.length(); j++) {
                if (set.contains(i + ":" + j)) {
                    if (j < s2.length() && (Character.toUpperCase(s1.charAt(i)) == s2.charAt(j)))
                        set.add((i + 1) + ":" + (j + 1));
                    if (!Character.isUpperCase(s1.charAt(i)))
                        set.add((i + 1) + ":" + j);
                }
            }
        }
        System.out.println(set);
        return set.contains(n + ":" + m);
    }


    public static void main(String[] args) {
        String s1 = "daBcdq";
        String s2 = "ABC";
        if (check(s1, s2))
            System.out.println("YES");
        else
            System.out.println("NO");

    }
}

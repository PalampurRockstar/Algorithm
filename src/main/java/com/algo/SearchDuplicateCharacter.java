package com.algo;

import com.sun.org.apache.xpath.internal.operations.Bool;

import java.util.HashMap;
import java.util.Map;

public class SearchDuplicateCharacter {

    public static void main(String[] args) {
        String name = "sourabhRaghav";
        Map<Character, Boolean> exist = new HashMap<>();
        for (int i = 0; i < name.length(); ++i) {
            if (exist.containsKey(name.charAt(i))) {
                System.out.println("Found : " + name.charAt(i) + " at : " + i);
                break;
            } else
                exist.put(name.charAt(i), true);
        }

    }
}

package com.algo;

import java.util.HashMap;
import java.util.Map;

public class SubStringContainUniqueCharacter {
    static Map<Character, Integer> toFindMap = new HashMap<Character, Integer>();
    static String list;
    static String toFind;
    static int backIndex = 0;
    static int frontIndex = 0;
    static int foundWordCount = 0;
    static int requiredWordCount;
    static int minDistance = Integer.MAX_VALUE;
    static int snapShotBackIndex = -1;
    static int snapShotFrontIndex = -1;

    public static void main(String[] args) {
        String result = findSmallestUniqueWindow("tutorial cup", "oti");
        System.out.println("result: " + result);
    }

    public static String findSmallestUniqueWindow(String firstString, String secondString) {
        list = firstString;
        toFind = secondString;
        requiredWordCount = toFind.length();

        initiaizeToFindMap();

        while (frontIndex < list.length()) {
            traverse();
            if (foundWordCount == requiredWordCount) {
                shrinkIfPossible();
                clickSnapShot();
            }
            frontIndex++;
        }
        if (snapShotFrontIndex != -1 && snapShotFrontIndex != -1) {
            return list.substring(snapShotBackIndex, snapShotFrontIndex + 1);
        } else {
            return null;
        }
    }

    static void initiaizeToFindMap() {
        for (int i = 0; i < toFind.length(); ++i) {
            toFindMap.put(toFind.charAt(i), 0);
        }
    }

    private static void shrinkIfPossible() {
        while (!toFindMap.containsKey(list.charAt(backIndex)) || toFindMap.get(list.charAt(backIndex)) != 1) {
            if (toFindMap.containsKey(list.charAt(backIndex)))
                toFindMap.put(list.charAt(backIndex), toFindMap.get(list.charAt(backIndex)) - 1);
            backIndex++;
        }
    }

    private static void traverse() {
        char currentChar = list.charAt(frontIndex);
        if (toFindMap.containsKey(currentChar)) {
            toFindMap.put(currentChar, toFindMap.get(currentChar) + 1);
            if (toFindMap.get(currentChar) == 1)
                foundWordCount++;
        }
    }

    static void clickSnapShot() {
        if (minDistance > (frontIndex - backIndex + 1)) {
            snapShotFrontIndex = frontIndex;
            snapShotBackIndex = backIndex;
            minDistance = (frontIndex - backIndex + 1);
        }
    }


}
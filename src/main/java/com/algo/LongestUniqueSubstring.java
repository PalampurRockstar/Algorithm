package com.algo;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class LongestUniqueSubstring {
    static String list;
    static Set set;
    static int longestSubstring;
    static int frontIndex;
    static int backIndex;
    static int snapShotBack;
    static int snapShotFront;


    public static void main(String[] args) {
        System.out.println(lengthOfLongestSubstring("tmmzuxt"));
//        System.out.println(longestUniqueSubString("abcabcbb"));
    }



    static void init() {
        longestSubstring = 0;
        set = new HashSet<Character>();
        frontIndex = 0;
        backIndex = 0;
        snapShotBack = -1;
        snapShotFront = -1;
    }

    public static int lengthOfLongestSubstring(String input) {

        init();
        list = input;
        while (frontIndex < list.length()) {
            if (traverseAndDecideShrink()) {
                shrinkWindow();
            }
            snapShot();
            frontIndex++;
        }
        if (snapShotBack != -1 && snapShotFront != -1) {
            System.out.println("snapShotBack: "+snapShotBack +" : snapShotFront : "+snapShotFront);
            System.out.println("string : " + list.substring(snapShotBack, snapShotFront+1));
        }
        return longestSubstring;
    }

    static void snapShot() {
        System.out.println(frontIndex + " : " + backIndex + " : " + (frontIndex - backIndex));
        if (longestSubstring < (frontIndex - backIndex + 1)) {
            snapShotBack = backIndex;
            snapShotFront = frontIndex;
            longestSubstring = (frontIndex - backIndex + 1);
        }
    }

    static boolean traverseAndDecideShrink() {
        char current = list.charAt(frontIndex);
        if (set.contains(current)) {
            System.out.println("not found : " + current);
            return true;
        } else {
            System.out.println("found : " + current);
            set.add(current);
            return false;
        }
    }

    static void shrinkWindow() {

        while (list.charAt(backIndex) != list.charAt(frontIndex)) {
            backIndex++;
        }
        backIndex++;
    }
    static int longestUniqueSubString(String list){

        Map<Character, Integer> seen = new HashMap<>();
        int maximum_length = 0;
        int back = 0;

        for(int front = 0; front < list.length(); front++){
            char current=list.charAt(front);
            if(seen.containsKey(current))
                back = Math.max(back, seen.get(list.charAt(front)) + 1);

            seen.put(current, front);
            if(maximum_length<front-back + 1){
                snapShotBack=back;
                snapShotFront=front;
            }
            maximum_length = Math.max(maximum_length, front-back + 1);
        }
        if (snapShotBack != -1 && snapShotFront != -1) {
            System.out.println("snapShotBack: "+snapShotBack +" : snapShotFront : "+snapShotFront);
            System.out.println("string : " + list.substring(snapShotBack, snapShotFront+1));
        }
        return maximum_length;
    }
}

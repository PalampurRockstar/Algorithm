package com.algo;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class ConvertSentenceWithoutSpaceToSpacedHavingValidWords {
    public static void main(String[] args) {
        String input = "iamace";
        Set<String> dict = new HashSet<>();
        Map<String, String> cache = new HashMap<>();
        dict.add("i");
        dict.add("am");
        dict.add("ace");
        dict.add("a");

        String topDown = getSpacedSentence(input, dict, cache);
        System.out.println("Result  topDown:"+topDown);
        String bottomUp = bottomUp(input, dict);
        System.out.println("Result  bottomUp:"+bottomUp);
    }


    private static String bottomUp(String input, Set<String> dict) {
        int len = input.length();
        int possible[][] = new int[len][len];
        for (int i = 0; i < len; ++i) {
            for (int j = 0; j < len; ++j)
                possible[i][j] = -1;
        }
        for (int i = 0; i < len; ++i) {
            for (int j = 0; j < len - i; ++j) {
                int k = j + i;
                System.out.print(j + ":" + k + "\t");
                if (dict.contains(input.substring(j, k + 1))) {
                    System.out.println();
                    System.out.println("Found : " + input.substring(j, k + 1));
                    //can put index of i also to trace back the
                    possible[j][k] = j;
                } else {
                    System.out.println();
                    System.out.println(input.substring(j, k + 1) + " : to search");
                    for (int h = j; h < k; ++h) {
                        System.out.println(input.substring(j, h + 1) + ":" + input.substring(h + 1, k + 1));
                        if (possible[j][h] != -1 && possible[h + 1][k] != -1) {
                            possible[j][k] = h + 1;
                            break;
                        }
                    }
                }
            }
            System.out.println();
        }
        int back = 0;
        int front = len - 1;
        StringBuffer buffer = new StringBuffer();
        while (back < front) {
            System.out.println(back + ":" + front + ":" + possible[back][front] + " =" + input.substring(back, possible[back][front] + 1));
            int k = possible[back][front];
            if (back == k) {
                buffer.append(input.substring(back, front + 1));
                break;
            }
            buffer.append(input.substring(back, k) + " ");
            back = k;
        }
        return buffer.toString();

    }



    private static String getSpacedSentence(String input, Set<String> set, Map<String, String> cache) {
        if (cache.containsKey(input))
            return cache.get(input);
        for (int i = 0; i < input.length(); ++i) {
            if (set.contains(input.substring(0, i + 1))) {
                String right = getSpacedSentence(input.substring(i + 1), set, cache);
                //if right response is null and string length is more then 0 that mean fail to convert so return null
                if (input.substring(i + 1).length() > 0 && right == null) {
                    cache.put(input, null);
                    return cache.get(input);
                }
                //if right length is 0 and return null so discard it
                cache.put(input, right != null ?
                        input.substring(0, i + 1) + " " + right :
                        input.substring(0, i + 1));
                return cache.get(input);
            }
        }
        cache.put(input, null);
        return cache.get(input);
    }


}

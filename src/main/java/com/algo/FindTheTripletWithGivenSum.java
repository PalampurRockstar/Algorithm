package com.algo;

import java.util.Arrays;
import java.util.Collections;

public class FindTheTripletWithGivenSum {

    public static void main(String[] args) {
        int list[] = new int[]{2, 5, 6, 3, 7, 4, 0, 1};
        boolean result = findTriplet(list, 8);
    }

    private static boolean findTriplet(int[] list, int given) {
        Arrays.sort(list);
        boolean found = false;
        for (int i = 0, right = list.length - 1; i < list.length - 2; ++i) {
            int left = i + 1;
            while (left < right) {
                if (list[i] + list[right] + list[left] == given) {
                    found = true;
                    System.out.println(list[i] + ": " + list[right] + ":" + list[left]);
                    break;
                } else if (list[i] + list[right] + list[left] < given) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        return found;
    }

}

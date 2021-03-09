package com.algo;

public class LargestUniqueWindow {

	public static void main(String[] args) {
		int foundCharacterIndex[] = new int[256];
		String str = "this is a testwindow";
		for (int i = 0; i < str.length(); ++i) {
			System.out.print(str.charAt(i) + "  ");
		}
		System.out.println();
		for (int i = 0; i < str.length(); ++i) {
			System.out.print(i + "  ");
		}
		System.out.println();
		findLargestUniqueWindow(str);
	}

	private static void findLargestUniqueWindow(String str) {
		int foundCharacterIndex[] = new int[256];

		str = " " + str.toLowerCase();
		int max = Integer.MIN_VALUE, maxStart = -1, maxEnd = -1;

		int start = 0, end = 0;
		for (int i = 0; i < str.length(); ++i) {
			char c = str.charAt(i);
			if (foundCharacterIndex[((int) c)] == 0) {
				foundCharacterIndex[((int) c)] = i;
				start = i;
			} else {

				end = foundCharacterIndex[((int) c)] + 1;
			}
			if (max < (start - end)) {
				max = start - end;
				maxStart = start;
				maxEnd = end;
			}
		}
		maxEnd--;
		maxStart--;
		System.out.println("max : " + max);
		System.out.println(maxEnd + " : " + maxStart);
	}
}

package com.algo;

public class SubStringContainAnotherStringConsideringCount {
	public static void main(String[] args) {
		String str = "this ttis a test string";
		String pattern = "tist";
		String response = minWindow(str, pattern);
		System.out.println(response);
	}

	public static String minWindow(String str, String pattern) {
		int sLen = str.length();
		int tLen = pattern.length();

		// initialize needToFind array
		int[] needToFind = new int[256];
		for (int i = 0; i < tLen; i++) {
			needToFind[pattern.charAt(i)]++;
		}

		int[] hasFound = new int[256];
		int minWinLen = Integer.MAX_VALUE;
		int minWinBegin = 0;
		int minWinEnd = 0;
		int count = 0;
		for (int end = 0, start = 0; start < sLen; start++) {
			if (needToFind[str.charAt(start)] != 0) {
				hasFound[str.charAt(start)]++;
				System.out.println("Front char : " + str.charAt(start));
				if (hasFound[str.charAt(start)] <= needToFind[str.charAt(start)])
					count++;

				if (count == tLen) {
					while (needToFind[str.charAt(end)] == 0 || hasFound[str.charAt(end)] > needToFind[str.charAt(end)]) {
						System.out.println("Back char : " + str.charAt(end));
						if (hasFound[str.charAt(end)] > needToFind[str.charAt(end)])
							hasFound[str.charAt(end)]--;
						end++;
						System.out.println("Increasing end-> : " + end);
					}

					if (start - end + 1 < minWinLen) {
						System.out.println("snapshot : " + end + " : " + start);
						minWinBegin = end;
						minWinEnd = start;
						minWinLen = start - end + 1;
					}
				}
			}
			System.out.println("Increasing start-> : " + (start + 1));
		}
		return (count == tLen) ? str.substring(minWinBegin, minWinEnd + 1) : "";
	}
}

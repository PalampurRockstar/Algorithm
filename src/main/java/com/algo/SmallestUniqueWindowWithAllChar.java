package com;



public class SmallestUniqueWindowWithAllChar {

	
	public static void main(String[] args) {
		String str = "this this is a test stringgg";
		String window = findSmallestWndow(str);
		System.out.println("Result : " + window);

	}

	private static String findSmallestWndow(String input) {

		int countUnique = 0;
		int no_of_chars = 256;
		int charCount[] = new int[no_of_chars];
		for (int i = 0; i < input.length(); ++i) {
			int index = input.charAt(i);
			charCount[index]++;
			if (charCount[index] == 1) {
				countUnique++;
			}
		}
		
		return findSubSet(input, charCount, countUnique);
	}

	private static String findSubSet(String input, int[] charCount, int countUnique) {
		int[] startCharCount = charCount;
		int index = 0;
		boolean found = false;
		boolean left = true;
		int start = 0,end = 0;
		while (!found) {
			char each= input.charAt(index);
			if (left) 
				index++;
			 else 
				index--;
			if (startCharCount[each] > 1) {
				startCharCount[each]--;
			} else {
				if (left) {
					left = !left;
					start=index-1;
					index = input.length() - 1;
				} else {
					end=index+2;
					found=true;
				}
			}
		}

		return input.substring(start, end);
	}
}

package com.algo;

public class QuickSort {
	public static void main(String[] args) {
		int list[] = { 6, 5, 8, 9, 3, 10, 15, 12, 16 };
		list = sort(list, 0, list.length - 1);
		for (int i : list) {
			System.out.println(i);
		}
	}

	public static int[] sort(int temp_array[], int low_index, int high_index) {

		int i = low_index;
		int j = high_index;
		// calculate pivot number
		int pivot = temp_array[low_index + (high_index - low_index) / 2];
		// Divide into two arrays
		while (i <= j) {
			while (temp_array[i] < pivot) {
				i++;
			}
			while (temp_array[j] > pivot) {
				j--;
			}
			if (i <= j) {
				swap(temp_array, i, j);
				// move index to next position on both sides
				i++;
				j--;
			}
		}
		// call quickSort() method recursively
		if (low_index < j)
			sort(temp_array, low_index, j);
		if (i < high_index)
			sort(temp_array, i, high_index);
		return temp_array;
	}

	public static void swap(int temp_array[], int i, int j) {
		int temp = temp_array[i];
		temp_array[i] = temp_array[j];
		temp_array[j] = temp;
	}

}

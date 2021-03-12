package com.algo;

import static org.junit.Assert.*;

import org.junit.Test;

public class SortTest {

	@Test
	public void test() {

		int list[] = { 6, 5, 8, 9, 3, 10, 15, 12, 16 };
		int actual[] = QuickSort.sort(list, 0, list.length - 1);
		int expected[] = { 3, 5, 6, 8, 9, 10, 12, 15, 16 };
		assertArrayEquals(expected, actual);
	}

}

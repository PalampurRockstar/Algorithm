package com.algo;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class SmallestWindowTest {

	@Test
	public void test() {
		String response = SubStringContainChar.minWindow("this ttis a test string", "tist");
		System.out.println(response);
		assertEquals("ttis", response);
		response=SubStringContainChar.minWindow("this is a test string", "tist");
		System.out.println(response);
		assertEquals("t stri", response);
	}

}

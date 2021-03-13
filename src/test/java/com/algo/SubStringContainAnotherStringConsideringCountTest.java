package com.algo;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class SubStringContainAnotherStringConsideringCountTest {

	@Test
	public void test() {
		String response = SubStringContainAnotherStringConsideringCount.minWindow("this ttis a test string", "tist");
		System.out.println(response);
		assertEquals("ttis", response);
		response= SubStringContainAnotherStringConsideringCount.minWindow("this is a test string", "tist");
		System.out.println(response);
		assertEquals("t stri", response);
	}

}

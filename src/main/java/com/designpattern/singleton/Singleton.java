package com.designpattern.singleton;

import java.util.ArrayList;
import java.util.List;

public class Singleton {
	private Singleton() {
	}

	private static List<Integer> list;

	public static List<Integer> getInstance() {
		if (list == null) {
			list = new ArrayList<Integer>();
		}
		return list;
	}
}

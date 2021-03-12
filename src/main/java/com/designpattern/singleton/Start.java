package com.designpattern.singleton;

import java.util.List;

public class Start {

	public static void main(String[] args) {
		List<Integer> list=Singleton.getInstance();
		list.add(34);
		list.add(56);
		list.forEach(System.out::println);
		list.remove(0);
		List<Integer> list2=Singleton.getInstance();
		list2.forEach(System.out::println);
		
	}
}

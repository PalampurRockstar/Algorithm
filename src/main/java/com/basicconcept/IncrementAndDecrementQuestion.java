package com.basicconcept;

public class IncrementAndDecrementQuestion {
	public static void main(String[] args) {
		B o = new B();
	}
}

class A {
	static int i = 1;
	static {
		i = i++ - ++i;
		System.out.println("First  A : " + i);
	}
	{
		System.out.println("Second Block A");
	}

	public A() {
		System.out.println("Constructor A");
	}
}

class B extends A {
	static {
		i = i++ - ++i;
		System.out.println("Third  B : " + i);
	}
	{
		System.out.println("Fourth Block B");
	}

	public B() {
		System.out.println("Constructor B");
	}

	public static void main(String[] args) {
		B o = new B();

	}
}
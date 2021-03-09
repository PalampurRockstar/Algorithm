package com.designpattern.decorator;

public interface Car {
	void design();
}

class Maruti implements Car {

	@Override
	public void design() {
		System.out.println("4 Type + chassis");
	}
	
}
class BMW implements Car {

	@Override
	public void design() {
		System.out.println("BMW");
	}
}

package com.designpattern.decorator;

public class LooksDecorator implements Car {
	Car car;

	public LooksDecorator(Car car) {
		this.car = car;
	}

	@Override
	public void design() {
		System.out.println("Modified looks");
		car.design();
		System.out.println("High end interior");
	}
}

package com.designpattern.facade;

public class CarMaker {
	Car bmw;
	Car toyota;

	public CarMaker() {
		this.bmw = new BMW();
		this.toyota = new Toyota();
	}

	public Car getBmw() {
		return bmw;
	}

	

	public Car getToyota() {
		return toyota;
	}


}

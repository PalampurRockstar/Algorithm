package com.designpattern.decorator;

public class Start {
	public static void main(String[] args) {
		Maruti maruti = new Maruti();
		maruti.design();
		System.out.println("---------------------");
		
		BMW bmw = new BMW();
		bmw.design();
		System.out.println("---------------------");

		LooksDecorator newLookBMW = new LooksDecorator(bmw);
		newLookBMW.design();
		System.out.println("---------------------");
		
		LooksDecorator newLookMaruti = new LooksDecorator(maruti);
		newLookMaruti.design();
		System.out.println("---------------------");

	}
}

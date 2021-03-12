package com.designpattern.facade;

public class FacadeDemo {
	public static void main(String[] args) {
		CarMaker cm=new CarMaker();
		cm.getToyota().design();
		cm.getBmw().design();
	}
}

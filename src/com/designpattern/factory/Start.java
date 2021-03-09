package com.designpattern.factory;

public class Start {
	public static void main(String[] args) {
		Factory hmv = FactoryProvider.getFactory(true);
		Factory lmv = FactoryProvider.getFactory(false);
		Vehicle motorcycle = lmv.getInstance("motorcycle");
		motorcycle.vehicleType();
		Vehicle car = hmv.getInstance("car");
		car.vehicleType();
	}
}

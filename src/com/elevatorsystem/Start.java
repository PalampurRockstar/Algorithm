package com.elevatorsystem;

public class Start {
	public static void main(String[] args) {
		ElevatorSystem es=new ElevatorSystem(4,20,0);
		es.start();
		es.requestCar(new Request(Direction.DOWN,5));
		es.requestCar(new Request(Direction.DOWN,7));
		es.requestCar(new Request(Direction.UP,2));
		
	}
}

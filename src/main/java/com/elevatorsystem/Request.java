package com.elevatorsystem;

public class Request implements Comparable<Request> {

	public Request(Direction direction, int floor) {
		super();
		this.direction = direction;
		this.floor = floor;
	}

	public Direction direction;
	public int floor;

	@Override
	public int compareTo(Request o) {
		return this.floor - o.floor;
	}
}

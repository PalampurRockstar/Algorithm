package com.elevatorsystem;

import java.util.LinkedHashSet;
import java.util.Set;

public class Elevator extends Thread {
	int elevatorId;
	Set<Request> requestList;
	int targetFloor;
	int currentFloor;
	int totalFloor;
	Direction direction;

	public Elevator(int elevatorId, int totalFloor) {
		this.elevatorId = elevatorId;
		this.totalFloor = totalFloor;
		requestList = new LinkedHashSet<Request>();
	}

	@Override
	public void run() {
		while (true) {
			while (!requestList.isEmpty()) {
				if (direction == Direction.UP) {
					
				}
			}
		}
	}

	private void pause() {

	}

	private void waitingToStart() {

	}

	void move() {
		if (direction == Direction.UP) {
			goUp();
		} else if (direction == Direction.DOWN) {
			goDown();
		}
	}

	private void goUp() {
		for (int i = currentFloor; i <= targetFloor; ++i) {
			try {
				Thread.sleep(200);
				System.out.println(currentFloor);
			} catch (InterruptedException e) {

				e.printStackTrace();
			}
		}
	}

	private void goDown() {
		int initialRequestSize = requestList.size();
		for (int i = currentFloor; i >= targetFloor; --i) {
			try {
				Thread.sleep(200);
				System.out.println(currentFloor);
				if (initialRequestSize != requestList.size()) {

				}
			} catch (InterruptedException e) {

				e.printStackTrace();
			}
		}

	}

	public void getElevatorStatus() {

	}

	public void addRequest(Request request) {
		requestList.add(request);
		if (distanceToCover(request.floor) < distanceToCover(targetFloor)) {
			targetFloor = request.floor;
		}

	}

	private int distanceToCover(int floor) {
		return 7;
	}

}

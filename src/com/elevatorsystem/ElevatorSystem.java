package com.elevatorsystem;

import java.util.ArrayList;
import java.util.List;

public class ElevatorSystem {

	public ElevatorSystem(int totalElevator, int totalFloor, int initialFloor) {
		this.initialFloor = initialFloor;
		this.totalFloor = totalFloor;
		this.totalElevator = totalElevator;
		elevatorList = new ArrayList<Elevator>();
		for (int i = 0; i < totalElevator; ++i) {
			elevatorList.add(new Elevator(i, totalFloor));
		}

	}

	List<Elevator> elevatorList;
	int totalFloor;
	int totalElevator;
	int initialFloor;

	public void start() {
		for (Elevator each : elevatorList) {
			each.start();
		}
	}

	public void requestCar(Request request) {
		int elevatorNumber = getSuitableElebatorFor(request);
		elevatorList.get(elevatorNumber).addRequest(request);
	}

	private int getSuitableElebatorFor(Request request) {
		for (Elevator each : elevatorList) {
			each.getElevatorStatus();
		}
		return 0;

	}

}

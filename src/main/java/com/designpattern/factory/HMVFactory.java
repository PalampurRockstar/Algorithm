package com.designpattern.factory;

public class HMVFactory implements Factory {

	@Override
	public Vehicle getInstance(String instanceName) {
		if (instanceName.equals("car")) {
			return new Car();
		}
		return null;
	}

}

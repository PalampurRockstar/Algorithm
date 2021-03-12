package com.designpattern.factory;

public class LMVFactory implements Factory {

	@Override
	public Vehicle getInstance(String instanceName) {
		if(instanceName.equals("motorcycle")){
			return new MotorCycle();
		}
		return null;
	}

}
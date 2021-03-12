package com.designpattern.factory;

public class FactoryProvider {
	
	public static Factory getFactory(boolean decision) {
		if (decision) {
			return new HMVFactory();
		} else {
			return new LMVFactory();
		}
	}
}

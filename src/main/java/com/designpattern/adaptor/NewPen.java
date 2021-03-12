package com.designpattern.adaptor;

public interface NewPen {

	void writeFast();
}

class PilotPen implements NewPen {

	@Override
	public void writeFast() {
		System.out.println("PilotPen");
	}
}

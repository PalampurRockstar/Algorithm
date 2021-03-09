package com.designpattern.adaptor;

public interface OldPen {
	void writeSlow();
}

class InkPen implements OldPen {
	@Override
	public void writeSlow() {
		System.out.println("InkPen");
	}
}

package com.designpattern.adaptor;

public class Start {

	public static void main(String[] args) {
		OldPen inkPen = new InkPen();
		inkPen.writeSlow();
		NewPen pilotPen = new PilotPen();
		pilotPen.writeFast();

		OldToNewPen advancePen = new OldToNewPen(inkPen);
		advancePen.writeFast();

	}
}

class OldToNewPen implements NewPen {
	OldPen oldpen;

	public OldToNewPen(OldPen oldpen) {
		this.oldpen = oldpen;
	}

	@Override
	public void writeFast() {
		oldpen.writeSlow();
	}
}

package com.designpattern.builder;

public class Phone {
	private int id;
	private String type;
	private String brand;

	
	public Phone(int id, String type, String brand) {
		super();
		this.id = id;
		this.type = type;
		this.brand = brand;
	}

	
}
 class BuilderPhone {
	int id;
	String type;
	String brand;

	public BuilderPhone setId(int id) {
		this.id = id;
		return this;
	}

	public BuilderPhone setType(String type) {
		this.type = type;
		return this;
	}

	public BuilderPhone setBrand(String brand) {
		this.brand = brand;
		return this;
	}

	Phone getPhone() {
		return new Phone(id, brand, brand);
	}

}


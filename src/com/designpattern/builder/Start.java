package com.designpattern.builder;


public class Start {
	public static void main(String[] args) {
		
		BuilderPhone pb=new BuilderPhone();
		Phone phone=pb.setBrand("Apple").setId(3).getPhone();
		
		System.out.println(phone);;
	}
}

package com.algo;

public class SearchDuplicateCharacter {

	public static void main(String[] args) {
		String name="sourabhRaghav";
		boolean foundList[]=new boolean [26];
		name=name.toLowerCase();
		char paddingDecider='a';
		int padding=(int)paddingDecider;
		System.out.println(padding); 	
		for (int i=0;i<name.length();++i){
			int index=(int)name.charAt(i)-padding;
			if(foundList[index]){
				System.out.println("Found : "+name.charAt(i)+" at : "+i);
				break;
			}else
				foundList[index]=true;
		}
		
	}
}

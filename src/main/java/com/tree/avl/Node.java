package com.tree.avl;

public class Node {
	public int data;
	public int height = 0;
	public Node right;
	public Node left;

	public Node(int data) {
		this.data = data;
		right = null;
		left = null;
		height = 1;
	}
}

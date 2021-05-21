package com.avltst;

class Node {
	public Node(int data) {
		this.data = data;
		height = 1;
	}
	Node right;
	Node left;
	int data;
	int height = 0;
}

class AVLTree {
	Node node;

	public void insert(int data) {
		Node node = insertData(null, data);
	}

	private Node insertData(Node node, int data) {
		if (node == null) {
			return new Node(data);
		}
		if (data < node.data) {
			node.left = insertData(node.left, data);
		} else {
			node.right = insertData(node.right, data);
		}
		node.height = Integer.max(getHeight(node.left), getHeight(node.right)) + 1;

		return node;
	}

	private int getHeight(Node node) {
		if (node != null)
			return node.height;
		else
			return 0;
	}

	public void preorderTraversal() {

	}
}

public class AVLTreeExample {
	public static void main(String[] args) {
		AVLTree avl = new AVLTree();
		avl.insert(10);
		avl.insert(20);
		avl.insert(30);
		avl.preorderTraversal();
		avl.insert(40);
		avl.insert(50);
		avl.preorderTraversal();
		avl.insert(25);
		avl.preorderTraversal();

	}
}
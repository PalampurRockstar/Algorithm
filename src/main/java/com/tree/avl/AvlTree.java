package com.tree.avl;

public class AvlTree {
	Node avlNode;

	public static void main(String[] args) {
		AvlTree tree = new AvlTree();
		tree.insertData(10);
		tree.insertData(20);
		tree.insertData(30);
		tree.insertData(40);
		tree.insertData(50);
		tree.insertData(25);
		tree.print();
	}

	public void print() {
		inOrder(avlNode);
		preOrder(avlNode);

	}

	void preOrder(Node root) {
		if (root != null) {
			System.out.print(root.data + " ");
			preOrder(root.left);
			preOrder(root.right);
		}
	}

	void inOrder(Node root) {
		if (root != null) {
			inOrder(root.left);
			System.out.print(root.data + " ");
			inOrder(root.right);
		}
	}

	private void insertData(int data) {

		this.avlNode = insert(this.avlNode, data);
	}

	private Node insert(Node node, int data) {
		if (node == null) {
			return new Node(data);
		} else {
			if (node.data > data) {
				node.left = insert(node.left, data);
			} else {
				node.right = insert(node.right, data);
			}
		}
		int lHeight = getHeight(node.left);
		int rHeight = getHeight(node.right);
		node.height = Integer.max(lHeight, rHeight) + 1;
		int balanceFactor = lHeight - rHeight;
		if (balanceFactor < -1 && data > node.right.data) {
			// RR
			node = rightRotation(node);
		} else if (balanceFactor < -1 && data < node.right.data) {
			// RL
			node.right = leftRotation(node.right);
			node = rightRotation(node);
		} else if (balanceFactor > 1 && data > node.right.data) {
			// LR
			node.left = rightRotation(node.left);
			node = leftRotation(node);
		} else if (balanceFactor > 1 && data < node.right.data) {
			// LL
			node = leftRotation(node);
		}
		return node;

	}

	Node leftRotation(Node x) {
		Node y = x.left;
		x.left = y.right;
		y.right = x;
		x.height = Integer.max(getHeight(x.right), getHeight(x.left)) + 1;
		y.height = Integer.max(getHeight(y.right), getHeight(y.left)) + 1;

		x = y;
		return x;

	}

	Node rightRotation(Node x) {
		Node y = x.right;
		x.right = y.left;
		y.left = x;

		x.height = Integer.max(getHeight(x.right), getHeight(x.left)) + 1;
		y.height = Integer.max(getHeight(y.right), getHeight(y.left)) + 1;

		x = y;
		return x;
	}

	public int getHeight(Node node) {
		if (node == null)
			return 0;
		return node.height;

	}
}

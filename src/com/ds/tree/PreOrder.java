package com.ds.tree;

import java.util.Stack;

public class PreOrder {
	Stack<Node> stack = new Stack<Node>();
	Node node;

	public PreOrder(Node node) {
		this.node = node;
	}

	public static void main(String[] args) {
		Node node = new Node(7);
		node.right = new Node(9);
		node.right.left = new Node(8);
		node.right.right = new Node(10);

		node.left = new Node(4);
		node.left.left = new Node(2);
		node.left.right = new Node(5);
		PreOrder orl = new PreOrder(node);
		orl.traverse();

	}

	private void traverse() {
		if (this.node != null) {
			stack.push(node);

			while (!stack.empty()) {
				Node current = stack.pop();
				System.out.println(current.data);

				if (current.right != null) {
					stack.push(current.right);
				}
				if (current.left != null) {
					stack.push(current.left);
				}
			}

		}
	}
}

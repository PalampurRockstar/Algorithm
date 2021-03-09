package com.ds.tree;

import java.util.Stack;

public class InOrder {
	Stack<Node> stack = new Stack<Node>();
	Node node;

	public InOrder(Node node) {
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
		InOrder lor = new InOrder(node);
		lor.traverse();

	}

	public void traverse() {

		stack.push(this.node);
		while (stack.peek().left != null) {
			stack.push(stack.peek().left);
		}
		while (!stack.empty()) {
			Node current = stack.pop();
			System.out.println(current.data);
			if (current.right != null) {
				stack.push(current.right);
				while (stack.peek().left != null) {
					stack.push(stack.peek().left);
				}
			}
		}

	}

}

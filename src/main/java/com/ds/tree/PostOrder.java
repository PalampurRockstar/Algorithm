package com.ds.tree;

import java.util.Stack;

public class PostOrder {
    Stack<Node> stack = new Stack<Node>();
    Node node;

    public PostOrder(Node node) {
        this.node = node;
    }

    public static void main(String[] args) {

        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);
        root.right.left = new Node(6);
        root.right.right = new Node(7);
        PostOrder lor = new PostOrder(node);
        lor.traverse();

    }

    public void traverse() {
        if (this.node != null) {
            Node prev = null;
            stack.push(this.node);
            while (!stack.isEmpty()) {
                Node current = stack.peek();
                if (current.left == prev) {
                    if (current.right != null) {
                        prev = current;
                        stack.push(current.right);
                    }
                } else if (current.right == prev) {
                    prev = stack.pop();
                    System.out.println(prev.data);
                } else if (current.left != null) {
                    prev = current;
                    stack.push(current.left);
                } else if (current.left == null) {
                    prev = stack.pop();
                    System.out.println(prev.data);
                }
            }
        }
    }

}

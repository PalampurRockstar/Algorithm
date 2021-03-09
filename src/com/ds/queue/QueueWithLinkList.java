package com.ds.queue;

public class QueueWithLinkList {
	QNode rear = null, front = null;

	public void queue(int data) {
		if (rear == null) {
			rear = new QNode(data);
			front = rear;
		} else {
			rear.next = new QNode(data);
			rear = rear.next;
		}
	}

	public boolean dequeue() {
		if (front == null) {
			System.out.println("Empty Queue :  Cannot Dequeue");
			return false;
		} else {
			front = front.next;
			return true;
		}
	}

	public void printAllNodes() {
		if (front != null) {
			QNode node = front;
			while (node != null) {
				System.out.println(node.data);
				node = node.next;
			}
		} else {
			System.out.println("Empty Queue : Cannot Display");
		}
	}

	public static void main(String[] args) {
		QueueWithLinkList q = new QueueWithLinkList();
		q.queue(4);
		q.queue(7);
		q.queue(26);
		q.printAllNodes();
		q.dequeue();
		q.dequeue();
		q.dequeue();
		q.dequeue();
		q.printAllNodes();
	}
}

class QNode {
	public QNode(int data) {
		this.data = data;
		this.next = null;
	}

	int data;
	QNode next;
}

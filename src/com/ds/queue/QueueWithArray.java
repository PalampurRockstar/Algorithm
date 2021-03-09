package com.ds.queue;

public class QueueWithArray {
	int queue[];
	int front, rear, capacity, currentSize;

	public QueueWithArray(int capacity) {
		this.capacity = capacity;
		queue = new int[capacity];
		front = -1;
		rear = -1;
	}

	public boolean isFull() {
		if (currentSize == capacity) {
			return true;
		} else
			return false;
	}

	public boolean isEmpty() {
		if (currentSize == 0) {
			front = -1;
			rear = -1;
			return true;
		} else
			return false;
	}

	public boolean queue(int number) {
		System.out.println("\nqueue : " + number);
		if (!isFull()) {
			if (isEmpty()) {
				front++;
			}
			rear++;
			rear = rear % capacity;
			queue[rear] = number;
			currentSize++;
			display();
			return true;
		} else {
			System.out.println("Queue full!");
			display();
			return false;
		}
	}

	public int dequeue() {
		System.out.println("\ndequeue");
		if (!isEmpty()) {
			int removedValue = queue[front];
			queue[front] = 0;
			front++;
			front = front % capacity;
			currentSize--;
			display();
			return removedValue;
		} else {
			System.out.println("Queue empty!!");
			display();
			return 999;

		}

	}

	public void display() {
		System.out.println();
		for (int i = 0; i < queue.length; ++i) {
			System.out.print(queue[i] + " ");
		}
	}

	public static void main(String[] args) {
		QueueWithArray q = new QueueWithArray(4);
		q.dequeue();
		q.queue(20);
		q.queue(30);
		q.queue(40);
		q.queue(50);
		q.queue(60);
		q.dequeue();
		q.dequeue();
		q.dequeue();
		q.queue(90);
		q.dequeue();
		q.dequeue();
		q.queue(90);
		q.dequeue();
		q.dequeue();
	}

}

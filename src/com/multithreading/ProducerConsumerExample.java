package com.multithreading;

//Java program to implement solution of producer 
//consumer problem. 

import java.util.LinkedList;

public class ProducerConsumerExample {
	public static void main(String[] args) throws InterruptedException {
		final PC pc = new PC();
		Thread t1 = new Thread(() -> {
			try {
				pc.produce();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		});
		Thread t2 = new Thread(() -> {
			try {
				pc.consume();
			} catch (InterruptedException e) {
				e.printStackTrace();

			}
		});
		t1.start();
		t2.start();
	}

	public static class PC {
		int value = 0;
		LinkedList<Integer> list = new LinkedList<>();
		int capacity = 2;
		public void produce() throws InterruptedException {
			while (true) {
				System.out.println("About to enter : produce synchronized block");
				synchronized (this) {
					if (list.size() == capacity)
						wait();
					System.out.println("Producer produced-" + value);
					list.add(value++);
					notify();
					Thread.sleep(1000);
				}
			}
		}
		public void consume() throws InterruptedException {
			while (true) {
				System.out.println("About to enter : consume synchronized block");
				synchronized (this) {
					if (list.size() == 0)
						wait();
					int val = list.removeFirst();
					System.out.println("Consumer consumed-" + val);
					notify();
					Thread.sleep(1000);
				}
			}
		}
	}
}

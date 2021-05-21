package com.linkList;

public class FindMidOfSinglyLinkList {
    static Node head = null;

    static class Node {
        int data;
        Node next;

        public Node(int data) {
            this.data = data;
        }
    }

    public static void main(String[] args) {
        head = insert(4);
        head = insert(6);
        head = insert(9);
        head = insert(12);
        head = insert(15);
        traverse();
        Node mid = findMid();
        System.out.println("\nMid : " + mid.data);

    }

    private static Node findMid() {
        Node singleStep = head;
        for (Node doubleStep = head; doubleStep != null && doubleStep.next != null; singleStep = singleStep.next, doubleStep = doubleStep.next.next)
            ;
        return singleStep;
    }

    static void traverse() {
        Node curent = head;
        while (curent != null) {
            System.out.print(curent.data + " \t");
            curent = curent.next;
        }
    }

    static Node insert(int data) {
        if (head == null)
            head = new Node(data);
        else {
            Node current = head;
            while (current.next != null)
                current = current.next;
            current.next = new Node(data);
        }
        return head;
    }
}

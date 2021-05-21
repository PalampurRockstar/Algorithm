package com.tree.avl;

import java.util.Arrays;

public class ConvertSortedListToBinaryTree {
    static class Node {
        Node(int data) {
            this.data = data;
        }

        int data;
        Node right;
        Node left;
    }

    public static void main(String[] args) {
        int list[] = new int[]{2, 4, 6, 7, 9, 10, 15, 20, 24, 29, 30};
        Node node = constructTree(list);
    }


    private static Node constructTree(int[] list) {
        if (list.length == 0) {
            return null;
        }
        int mid = list.length / 2;
        Node node = new Node(list[mid]);
        node.right = mid < list.length ? constructTree(Arrays.copyOfRange(list, mid + 1, list.length)) : null;
        node.left = mid > 0 ? constructTree(Arrays.copyOfRange(list, 0, mid - 1)) : null;
        return node;
    }
}

package com.trie;

import java.util.HashMap;
import java.util.Map;

public class Trie {
    Node root = new Node(false);

    class Node {
        Map<Character, Node> map;
        boolean isValidWord;

        Node(boolean isValidWord) {
            this.isValidWord = isValidWord;
            this.map = new HashMap<>();
        }
    }

    void insert(Node node, String str) {
        if (str.length() == 1)
            if (node.map.containsKey(str.charAt(0)))
                node.map.get(str.charAt(0)).isValidWord = true;
            else
                node.map.put(str.charAt(0), new Node(true));

        else if (node.map.containsKey(str.charAt(0)))
            insert(node.map.get(str.charAt(0)), str.substring(1, str.length()));
        else {
            Node child = new Node(false);
            node.map.put(str.charAt(0), child);
            insert(child, str.substring(1, str.length()));
        }
    }

    boolean searchWord(String str) {
        return search(root, str);
    }

    boolean search(Node node, String str) {
        if (node.map.containsKey(str.charAt(0)))
            if (str.length() == 1)
                return node.map.get(str.charAt(0)).isValidWord;
            else
                return search(node.map.get(str.charAt(0)), str.substring(1, str.length()));
        else return false;

    }

    public Trie(String dict[]) {
        for (String each : dict)
            insert(root, each);
    }

    public static void main(String[] args) {
        String dictionary[] = {"find", "fire", "geeks", "all", "for", "on", "geeks", "answers", "inter"};
        Trie t = new Trie(dictionary);
        System.out.println("fire: " + t.searchWord("fire"));
        System.out.println("find : " + t.searchWord("find"));
        System.out.println("some : " + t.searchWord("some"));
        System.out.println("inte : " + t.searchWord("inte"));
    }
}
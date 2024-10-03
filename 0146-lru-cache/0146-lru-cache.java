import java.util.HashMap;

class Node {
    int key;
    int value;
    Node next;
    Node prev;
    
    Node(int key, int value) {
        this.key = key;
        this.value = value;
        next = prev = null;
    }
}

class LRUCache {
    Node head;
    Node tail;
    HashMap<Integer, Node> mpp;
    int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        mpp = new HashMap<>();
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head.next = tail;
        tail.prev = head;
    }

    private void insertAfterHead(Node temp) {
        temp.next = head.next;
        temp.prev = head;
        head.next.prev = temp;
        head.next = temp;
    }

    private void deleteNode(Node node) {
        if (node == null) return;
        node.prev.next = node.next;
        node.next.prev = node.prev;
        node.next = null;
        node.prev = null;
    }

    public int get(int key) {
        if (!mpp.containsKey(key)) return -1;
        Node node = mpp.get(key);
        deleteNode(node);
        insertAfterHead(node);
        return node.value;
    }
    
    public void put(int key, int value) {
        if (mpp.containsKey(key)) {
            Node node = mpp.get(key);
            node.value = value;
            deleteNode(node);
            insertAfterHead(node);
        } else {
            Node newNode = new Node(key, value);
            if (mpp.size() == capacity) {
                Node lruNode = tail.prev;
                deleteNode(lruNode);
                mpp.remove(lruNode.key);
            }
            insertAfterHead(newNode);
            mpp.put(key, newNode);
        }
    }
}

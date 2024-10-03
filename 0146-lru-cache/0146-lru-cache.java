class Node {
    int key;    // Adding key to identify the node
    int value;  // Change 'data' to 'value' for clarity
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
    HashMap<Integer, Node> mpp; // Map to store key and Node
    int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        mpp = new HashMap<>();
        head = new Node(-1, -1); // Dummy head
        tail = new Node(-1, -1); // Dummy tail
        head.next = tail;
        tail.prev = head;
    }

    private void insertAfterHead(Node temp) {
        temp.next = head.next; // Link temp node's next to head's next node
        temp.prev = head;      // Set temp node's prev to head

        head.next.prev = temp; // If head's next exists, set its prev to temp
        head.next = temp;      // Link head to temp
    }

    private void deleteNode(Node node) {
        if (node == null) return;

        // Adjust the links of the previous and next nodes
        node.prev.next = node.next;
        node.next.prev = node.prev;

        // Clear the node's pointers (optional)
        node.next = null;
        node.prev = null;
    }

    public int get(int key) {
        if (!mpp.containsKey(key)) return -1; // Key does not exist

        // Key exists, retrieve the node and update its position
        Node node = mpp.get(key);
        deleteNode(node); // Remove node from its current position
        insertAfterHead(node); // Insert it after head

        return node.value; // Return the value
    }
    
    public void put(int key, int value) {
        if (mpp.containsKey(key)) {
            // Key exists, update the value
            Node node = mpp.get(key);
            node.value = value; // Update value
            deleteNode(node); // Remove node from its current position
            insertAfterHead(node); // Insert it after head
        } else {
            // Key does not exist
            Node newNode = new Node(key, value);
            if (mpp.size() == capacity) {
                // Cache is full, remove the least recently used item
                Node lruNode = tail.prev; // The node before tail is the LRU
                deleteNode(lruNode); // Remove LRU node from the list
                mpp.remove(lruNode.key); // Remove from HashMap
            }
            // Insert the new node
            insertAfterHead(newNode);
            mpp.put(key, newNode); // Add to the HashMap
        }
    }
}

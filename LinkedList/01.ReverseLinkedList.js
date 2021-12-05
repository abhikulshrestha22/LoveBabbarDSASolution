class Node {
  constructor(data) {
    this.next = null;
    this.data = data;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  push = (val) => {
    let node = new Node(val);
    if (this.head) {
      let current = this.head;
      while (current.next) {
        current = current.next;
      }
      current.next = node;
    } else {
      this.head = node;
    }
  };

  print = () => {
    let current = this.head;
    while (current) {
      console.log(current.data);
      current = current.next;
    }
  };

  reverse = () => {
    let current = this.head;
    let prev = null;
    while (current) {
      let next = current.next;
      current.next = prev;
      prev = current;
      current = next;
    }
    this.head = prev;
  };

  recurseReverse = () => {
    if (!this.head) {
      return;
    }
    this.recurseReverseUtil(this.head, null);
  };

  recurseReverseUtil = (current, prev) => {
    if (!current.next) {
      this.head = current;
      current.next = prev;
      return;
    }
    let next = current.next;
    current.next = prev;
    this.recurseReverseUtil(next, current);
  };
}

let ll1 = new LinkedList();
ll1.push(new Node(5));
ll1.push(new Node(10));
ll1.push(new Node(90));
ll1.print();
ll1.reverse();
ll1.print();
ll1.recurseReverse();
ll1.print();

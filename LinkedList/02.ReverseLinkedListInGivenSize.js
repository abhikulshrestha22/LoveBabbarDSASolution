class Node {
    constructor(data) {
      this.data = data;
      this.next = null;
    }
  }
  
  class Solution {
    /* Should do this in-place without altering the nodes' values.*/
    reverse(node, k) {
      if (!node) {
        return null;
      }
  
      let current = node;
      let next = current.next;
      let prev = null;
      let count = 0;
  
      while (current && count < k) {
        next = current.next;
        current.next = prev;
        prev = current;
        current = next;
        count += 1;
      }
  
      if (next) {
        node.next = this.reverse(next, k);
      }
      return prev;
    }
  }
  
  const printlist = (headLocal) => {
    let current = headLocal;
    let s = "";
    while (current) {
      s += current.data + " ";
      current = current.next;
    }
    console.log(s);
  };
  
  let n = 8;
  let input_arr = [1, 2, 3, 4, 5, 6, 7, 8];
  let head = new Node(input_arr[0]);
  let tail = head;
  for (let i = 1; i < n; i++) {
    tail.next = new Node(input_arr[i]);
    tail = tail.next;
  }
  
  printlist(head);
  let k1 = 3;
  let obj = new Solution();
  let newhead = obj.reverse(head, k1);
  printlist(newhead);
  
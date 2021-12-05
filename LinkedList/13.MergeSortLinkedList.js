class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}
class Solution {
  //Function to sort the given linked list using Merge Sort.
  mergeSort(head) {
    if (!head || !head.next) {
      return head;
    }
    //your code here
    let [first, second] = this.findMid(head);
    first = this.mergeSort(first);
    second = this.mergeSort(second);
    return this.merge(first, second);
  }

  merge(first, second) {
    if (!first) {
      return second;
    }
    if (!second) {
      return first;
    }
    let answer = null;

    if (first.data <= second.data) {
      answer = first;
      answer.next = this.merge(first.next, second);
    } else {
      answer = second;
      answer.next = this.merge(first, second.next);
    }
    return answer;
  }

  findMid(head) {
    let first = null;
    let second = null;
    if (!head) {
      return [null, null];
    }
    let fast = head;
    let slow = head;
    while (fast.next && fast.next.next) {
      slow = slow.next;
      fast = fast.next.next;
    }
    first = slow;
    second = slow.next;
    slow.next = null;
    return [head, second];
  }
}

let llhead = new Node(3);
let others = [5, 2, 4, 1];
let current = llhead;
for (let i = 0; i < others.length; i++) {
  let newItem = new Node(others[i]);
  current.next = newItem;
  current = current.next;
}

// print all
let soln = new Solution();
let answer = soln.mergeSort(llhead);
console.log(answer);

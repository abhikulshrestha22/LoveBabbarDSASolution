class Stack {
    constructor() {
       this.items = []
    }

    push(val) {
        this.items.push(val)
    }

    pop() {
        if(!this.items.length) {
            return "Stack is empty"
        }
        return this.items.pop()
    }

    peek() {
        if(!this.items.length) {
            return "Stack is empty"
        }
        return this.items[this.items.length-1]
    }

    print() {
        for(let i of this.items) {
            console.log(i)
        }
    }
}

stack = new Stack();
stack.push(2)
stack.push(1)
stack.push(3)
stack.print()
stack.pop()
stack.print()
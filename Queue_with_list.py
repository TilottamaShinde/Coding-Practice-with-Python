class Queue:
    def __init__(self):
        self.items =[]

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued {item} into the queue")

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.items[0]

    def display(self):
        print("Queue (front -> rear): ",self.items)


#Example
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.display()
print("Front element : ", queue.peek())
print("Dequeued element : ", queue.dequeue())


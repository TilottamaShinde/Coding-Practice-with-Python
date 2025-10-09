from collections import deque


class Queue:
    def __init(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item} in the queue")

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.popleft()

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def display(self):
        print("Queue (front -> rear): ", list(self.queue))

#Example usage

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.display()

print("Dequeued item : ",queue.dequeue())
print("Front element : ", queue.peek())
queue.display()



#linear queue
def initQueue(): #initiate queue
    global queue,front,back
    queue = [""]*5
    front = -1
    back = -1


def enqueue(item):
    global queue,front,back
    if isEmpty() == True: #check if empty
        front += 1
        back +=1
        queue[back] = item
    elif isFull() == True: #check if full
        return "The queue is full, cannot enqueue"
    else:
        back += 1
        queue[back] = item

def dequeue():
    global queue,front,back
    if isEmpty() == True: #check if empty
        return "The queue is empty, nothing to dequeue"
    elif front == back: #check if only 1 data left 
        front = -1
        back = -1
    else:
        front += 1

def isEmpty():
    return front == -1

def isFull():
    return back == 5 - 1

def size():
    if isEmpty() == True: #check if empty
        return 0
    else:
        return back - front + 1

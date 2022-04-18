#circular queue
def initQueue():
    global queue,front,back
    queue = [""]*5
    front = -1
    back = -1

def enqueue(item):
    global queue,front,back
    if (back == front - 1) or (front == 0 and back == len(queue)-1): #Queue full
        return "Queue is full"
    elif front == -1: #Queue empty
        front = 0
        back = 0
        queue[back] = item
    else: #Queue partially full
        back = (back+1)%len(queue)
        queue[back] = item

def dequeue():
    global queue,front,back
    if front == -1: #Queue full
        return "Queue is full"
    elif front == back: #front and back pointer on one item
        front = -1
        back = -1
        return "Dequeue performed"
    else:
        front = (front+1)%len(queue)
        return "Dequeue performed"

def Display():
    print(queue)
    print("front pointer: "+str(front))
    print("back pointer: "+str(back))
        
        

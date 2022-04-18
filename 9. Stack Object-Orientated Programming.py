#Stack object-orientated programming
class Stack:
    def __init__(self):
        self.Data = [""]*20
        self.Top = -1

    def IsEmpty(self):
        return self.Top == -1

    def IsFull(self):
        return self.Top == 19

    def Push(self, data):
        if self.IsFull() == True:
            return "Stack is full"
        self.Top += 1
        self.Data[self.Top] = data

    def Pop(self):
        if self.IsEmpty() == True:
            return "Stack is empty"
        poped_data = self.Data[self.Top]
        self.Top -= 1
        return poped_data

    def Peek(self):
        return self.Data[self.Top]

    def Size(self):
        return self.Top + 1

    def Display(self):
        print("Array: "+str(self.Data)+", Top pointer: "+str(self.Top))
    
    

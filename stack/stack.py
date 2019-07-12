class stackNode:
    def __init__(self,data):
        self.data = data
        self.downNode = None

class searchNode:
    def __init__(self):
        self.top = None
    def push(self, data):
        if self.top == None:
            self.top = stackNode(data)
        else:
            temp = stackNode(data)
            temp.downNode = self.top
            self.top = temp
    def pop(self):
        if self.top == None:
            return "No Data!"
        else:
            temp = self.top
            self.top = temp.downNode
            return temp.data
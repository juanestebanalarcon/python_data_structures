class Node():
    def __init__(self,data,next):
        self.data=data
        self.next=next
    def setNode(self):
        head_=None
        for count in range(1,10):
            head_=Node(count,head_)
        while head_ !=None:
            print(head_.data)
            head_=head_.next
Node(0,0).setNode()
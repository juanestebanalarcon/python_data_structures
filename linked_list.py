from nodes import Node as n 

class SinglyLinkedList:
    def __init__(self):
        self.tall=None
        self.size=0
    def append(self,data):
        node=n(data)
        if self.tall==None:
            self.tall=node 
        else:
            current=self.tall
            
            while current.next:
                current=current.next
            current.next=node 
            self.size+=1
    def size(self):
        return self.size
    def iter(self):
        current=self.tall
        while current:
            val=current.data
            current=current.next
            yield val 
    def delete(self,data):
        current=self.tall
        previus=self.tall

        while current:
            if current.data==data:
                if current==self.tall:
                    self.tall=current.next
                else:
                    previus.next=current.next
                    self.size-=1
                    return current.data
            previus=current
            current=current.next 
    def search(self,data):
        for node in self.iter():
            if data == node:
                print(f'Data {data} found!')
    def clear(self):
        self.tall=None
        self.size=0 


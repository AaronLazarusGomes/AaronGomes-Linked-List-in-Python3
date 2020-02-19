class Node:		#creating a class called "Node"
    def __init__(self, data, name):  #Initializing the Node and it would look like → |data|name|next →|
        self.data = data
        self.name = name
        self.next = None 	#pointer

    def getData(self):		#function that returns the data
        return self.data

    def getName(self):		#function that returns the name
        return self.name


class LinkedList:			#the main class
    def __init__(self):		#Initializing the head to none
        self.head = None

    def createL(self, data, name): 		#function to create a linked List 
        h = self.head
        p = h
        q = h

        if(h == None):
            h = Node(data, name)
        else:
            while(p != None):
                q = p
                p = p.next
            p = Node(data, name)
            q.next = p

        return h

    def insertL(self, nodeNew, position):		#function to insert a new Node into the existing linked list
        h = self.head
        p = h
        q = h
        counter = 0
        while(p != None):
            if(counter == position):
                break
            else:
                counter = counter + 1
                q = p
                p = p.next

        nodeNew.next = p
        q.next = nodeNew

        return h

    def printL(self):		#printing the entire linked list
        h = self.head
        while(h != None):
            print(h.getData(), h.getName(), "→", end=" ")
            h = h.next


li = LinkedList()			#} creating two instances of	
newList = LinkedList()		#} the LinkedList class (main one)

for i in range(5):			#taking input data from the user
    data = int(input('Enter: '))
    name = input('Enter name: ')
    li.head = li.createL(data, name)

d = int(input('Enter new: '))  #entering a new Node in the specified position
n = input('Enter name: ')
p = int(input('Enter the position: '))
newList.head = newList.createL(d, n)
li.insertL(newList.head, p-1)

li.printL() 

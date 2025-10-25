class ll:
    def __init__(self,data=None):
        self.data=data
        self.next=None

        #-------------------

    def display(self,head):
        current=head
        while current:
            print(current.data)
            current=current.next

    #----------------------
    def search(self,head,data):
        current=head
        cnt=0
        while current:
            if current.data==data:
                return cnt
            current=current.next
            cnt=cnt+1
        return cnt
    
    #-----------------------------------


    def insert_at_beg(self,head,data):
        if head is None:
            return ll(data)
        newnode=ll(data)
        newnode.next=head
        return newnode
    
    def insert_at_end(self,head,data):
        if head is None:
            return ll(data)
        newnode=ll(data)
        newnode.next=None
        current=head
        while current.next:
            current=current.next
        current.next=newnode
        return head
    
    def insert_after_node(self,prevnode,data):
        if prevnode is None:
            return ll(data)
        
        newnode=ll(data)

        newnode.next=prevnode.next
        prevnode.next=newnode

        return newnode
    
    #------------------------------------------------------------


    def delete_at_start(self,head):
        temp=head
        head=head.next
        return temp
    
    def delete_from_last(self,head):
        current=head
        while current.next:
            current=current.next
            if current.next.next==None:
                temp=current.next
                current.next=None
        return temp
    
    def delete_in_bet(self,head,prevnode,data):
        current=head
        while current.next!=data:
            current=current.next
        current.next=current.next.next

# Create linked list
llist = ll(1)
head = llist  # First node

# Insert nodes
head = llist.insert_at_end(head, 2)
head = llist.insert_at_end(head, 3)
head = llist.insert_at_beg(head, 0)

# Display list
llist.display(head)  # 0 -> 1 -> 2 -> 3 -> None
print("\n")
# Search
print(llist.search(head, 2))  # 2
print("\n")
# Delete node
head = llist.delete_at_start(head)
llist.display(head)  # 1 -> 2 -> 3 -> None

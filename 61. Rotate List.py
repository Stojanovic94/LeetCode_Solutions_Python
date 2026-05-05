class Solution:
    def rotateRight(self, head,k):
        if head is None or head.next is None:
            return head
        n=1
        last=head
        while(last.next!=None):
            n+=1
            last=last.next
        k=k%n
        if k==0:
            return head   
        t=head
        count=1
        while t is  not None:
            if count== (n-k):
                break
            count+=1
            t=t.next
        new_head=t.next
        t.next=None
        last.next=head   
        return new_head             
        
# 1472. Design Browser History
# Difficulty: Medium
# Solved using list
class BrowserHistory: 

    def __init__(self, homepage: str):
        self.list=[homepage]
        self.indx=0


    def visit(self, url: str) -> None:
        if len(self.list)>self.indx+1:
            self.list[self.indx+1]=url
        else:self.list.append(url)
        self.indx+=1
        if len(self.list)>self.indx+1:
            n=len(self.list)
            for i in range(n-self.indx-1):
                self.list.pop()
        
        

    def back(self, steps: int) -> str:
        if steps>self.indx:
            self.indx=0
            print("back",self.list,self.indx)
            return self.list[0]
        self.indx=self.indx-steps
        return self.list[self.indx]
        

    def forward(self, steps: int) -> str:
        if steps > (len(self.list)-self.indx-1):
            self.indx=len(self.list)-1
            return self.list[self.indx]
        self.indx=self.indx+steps
        return self.list[self.indx]


# Solved using Doubly Linked List
class TreeNode:
    def __init__(self, url, next=None, prev=None):
        self.url=url
        self.next=next
        self.prev=prev


class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr= TreeNode(homepage)


    def visit(self, url: str) -> None:
        self.curr.next = TreeNode(url,prev=self.curr)
        self.curr= self.curr.next
        

    def back(self, steps: int) -> str:
        while self.curr.prev and steps>0:
            self.curr= self.curr.prev
            steps-=1
        return self.curr.url


    def forward(self, steps: int) -> str:
        while self.curr.next and steps>0:
            self.curr= self.curr.next
            steps-=1
        return self.curr.url
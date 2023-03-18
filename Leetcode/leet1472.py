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

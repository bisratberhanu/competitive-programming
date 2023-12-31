class Robot:

    def __init__(self, width: int, height: int):
        self.width=width
        self.height= height
        self.perimeter= 2*(width+height)
        self.x=0
        self.y= 0
        #self.dir= ["East",'North','West','South']
        self.curdir= 'East'
        self.counter=0

    def step(self, num: int) -> None:
        if num!=0: self.counter+=1
        val= num%(self.perimeter-4)
        
        while val>0:
            if self.curdir=='East':
                if self.x==self.width-1:
                    self.curdir='North'
                    self.y+=1
                else:
                    self.x+=1
                val-=1
            elif self.curdir=='North':
                if self.y== self.height-1:
                    self.curdir= 'West'
                    self.x-=1
                else:
                    self.y+=1
                val-=1
            elif self.curdir=='West':
                if self.x==0:
                    self.curdir='South'
                    self.y-=1
                else:
                    self.x-=1
                val-=1
            elif self.curdir=='South':
                if self.y==0:
                    
                    self.curdir='East'
                    self.x+=1
                else:
                    self.y-=1
                val-=1
        #print(self.x,self.y)

                     
                


        

    def getPos(self) -> List[int]:
        
        return [self.x,self.y]
        

    def getDir(self) -> str:
        if self.counter==0: return 'East'
        if [self.x,self.y]==[0,0]:
            
            return 'South'
        
        return self.curdir
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
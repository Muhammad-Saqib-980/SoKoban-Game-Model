import queue
class Space:
    def __init__(self,x,y):
            self.x=x
            self.y=y
    

    def __str__(self):
        return "Space"
    

    def force(self,head,stage=None):
        #move left 
        if(self.x==head.x+1 and self.y==head.y):
            head.x=head.x+1
            return head
        #move right
        if(self.x==head.x-1 and self.y==head.y):
            head.x=head.x-1
            return head
        #move down
        if(self.x==head.x and self.y==head.y+1):
            head.y=head.y+1
            return head
        #move up
        if (self.x==head.x and self.y==head.y-1):
            head.y=head.y-1
            return head


class Wall:
    def __init__(self,x,y,stage=None):
            self.x=x
            self.y=y
    

    def __str__(self):
        return "Wall"
    

    def force(self,head,stage=None):
        return head


class Head:
    def __init__(self,x=0,y=0):
            self.x=x
            self.y=y


class Box:
    def __init__(self,x,y):
            self.x=x
            self.y=y
    

    def __str__(self):
        return "Box"
    

    def force(self,head,stage=None):
        
        pos=(self.y)*stage.row+self.x
        #move left 
        if(self.x==head.x+1 and self.y==head.y):
            num=(self.y)*stage.row+self.x+1
            if(stage.game[num].__str__()=="Space"):
                temp=stage.game[pos]
                stage.game[pos]=stage.game[num]
                stage.game[num]=temp
                self.x=self.x+1
                head.x=head.x+1
                stage.game[pos].x=stage.game[pos].x-1
        
            return head
            
        #move right
        if(self.x==head.x-1 and self.y==head.y):
            num=(self.y)*stage.row+self.x-1
            if(stage.game[num].__str__()=="Space"):
                temp=stage.game[pos]
                stage.game[pos]=stage.game[num]
                stage.game[num]=temp
                self.x=self.x-1
                head.x=head.x-1
                stage.game[pos].x=stage.game[pos].x+1

            return head
        #move down
        if(self.x==head.x and self.y==head.y+1):
            num=(self.y+1)*stage.row+self.x
            if(stage.game[num].__str__()=="Space"):
                temp=stage.game[pos]
                stage.game[pos]=stage.game[num]
                stage.game[num]=temp
                self.y=self.y+1
                head.y=head.y+1
                stage.game[pos].y=stage.game[pos].y-1
            return head
        #move up
        if (self.x==head.x and self.y==head.y-1):
            num=(self.y-1)*stage.row+self.x
            if(stage.game[num].__str__()=="Space"):
                temp=stage.game[pos]
                stage.game[pos]=stage.game[num]
                stage.game[num]=temp
                self.y=self.y-1
                head.y=head.y-1
                stage.game[pos].y=stage.game[pos].y+1

            return head


class Stage:
    def __init__(self):
        self.row=0
        self.col=0
        self.game=list()
        self.head=Head(0,0)
      
    def Stage1(self):
        self.row=8
        self.col=8
        self.game=list()
        self.head=Head(4,4)
        string="SSWWWSSSSSWSWSSSSSWSWWWWWWWBSBSWWSSBSWWWWWWWBWSSSSSWSWSSSSSWWWSS"
        num=0
        for c in string:
            if(c=='S'):
                self.game.insert(num,Space(num%self.row,num//self.col))
            elif(c=='W'):
                self.game.insert(num,Wall(num%self.row,num//self.col))
            elif(c=='B'):
                self.game.insert(num,Box(num%self.row,num//self.col))
            num+=1

    def Stage11(self):
        self.row=8
        self.col=8
        self.game=list()
        self.head=Head(3,1)
        string="SWWWWWSSSWSSSWWWWWSWBSSWWSBSSSSWWSSBBSWWWWWSWSWSSSWSSSWSSSWWWWWS"
        num=0
        for c in string:
            if(c=='S'):
                self.game.insert(num,Space(num%self.row,num//self.col))
            elif(c=='W'):
                self.game.insert(num,Wall(num%self.row,num//self.col))
            elif(c=='B'):
                self.game.insert(num,Box(num%self.row,num//self.col))
            num+=1

    def copy(self):
        stage=Stage()
        stage.row=self.row
        stage.col=self.col
        stage.head=Head(self.head.x,self.head.y)
        stage.game=list()
        num=self.row*self.col
        for i in range(0,num):
            if(self.game[i].__str__()=="Space"):
                  stage.game.append(Space(self.game[i].x,self.game[i].y))
            elif(self.game[i].__str__()=="Wall"):
                stage.game.append(Wall(self.game[i].x,self.game[i].y))
            elif(self.game[i].__str__()=="Box"):
                stage.game.append(Box(self.game[i].x,self.game[i].y))
            
        return stage

    def draw(self):
        num=self.row*self.col
        for i in range(0,num):
            if(i%self.row==0):
                print()
            if(self.game[i].__str__()=="Space"):
                if(i==(self.head.y*self.row +self.head.x)):
                    print('H',end='')
                else:
                    print(' ',end="")

            elif(self.game[i].__str__()=="Wall"):
                print('W',end="")

            elif(self.game[i].__str__()=="Box"):
                print('B',end="")

    def moveRight(self):
        temp=self.copy()
        num=(temp.head.y)*temp.row+(temp.head.x+1)
        temp.head=temp.game[num].force(temp.head,temp)
        return temp

    def moveLeft(self):
        stage=self.copy()
        num=(stage.head.y)*stage.row+(stage.head.x-1)
        stage.head=stage.game[num].force(stage.head,stage)
        return stage
    
    def moveUp(self):
        stage=self.copy()
        num=(stage.head.y-1)*stage.row+(stage.head.x)
        stage.head=stage.game[num].force(stage.head,stage)
        return stage
        
    def moveDown(self):
        stage=self.copy()
        num=(stage.head.y+1)*stage.row+(stage.head.x)
        stage.head=stage.game[num].force(stage.head,stage)
        return stage
    def __eq__(self,other):
        if(self.row==other.row and self.col==other.col):
            if(self.head.x==other.head.x and self.head.y==other.head.y):
                for i in range(0,self.row*self.col):
                    if(self.game[i].__str__() != other.game[i].__str__()):
                        return False
                return True
        return False
class Node:
    def __init__(self,stage,action="none",parent=None):
        self.stage=stage
        self.action=action
        self.parent=parent
    
    def __eq__(self,other):
        if(other==None):
            return False
        return self.stage==other.stage
        
if __name__ == "__main__":
    final=None 
    numOfBox=4
    positions=[11,30,33,52]
    stage=Stage()
    stage.Stage11()
    stage.draw()
    node=Node(stage)
    elist=list()
    q=queue.Queue()
    q.put(node)
    j=0
    while(q.empty()==False):
        print(j)
        j+=1
        node=q.get()
        elist.append(node)
        left=node.stage.moveLeft()
        right=node.stage.moveRight()
        up=node.stage.moveUp()
        down=node.stage.moveDown()
        childes=list()
        childes.append(Node(left,"Left",node))
        childes.append(Node(right,"Right",node))
        childes.append(Node(up,"Up",node))
        childes.append(Node(down,"Down",node))
        for child in childes:
            num=0
            for obj in child.stage.game:
                if(obj.__str__()=="Box" and (num not in positions)):
                    l=obj.y*child.stage.row +obj.x-1
                    r=obj.y*child.stage.row +obj.x+1
                    u=(obj.y-1)*child.stage.row+obj.x
                    d=(obj.y+1)*child.stage.row+obj.x
                    if(child.stage.game[r].__str__() =="Wall" and child.stage.game[u].__str__()=="Wall"):
                        elist.append(child)
                    elif(child.stage.game[l].__str__() =="Wall" and child.stage.game[u].__str__()=="Wall"):
                        elist.append(child)
                    elif(child.stage.game[r].__str__() =="Wall" and child.stage.game[d].__str__()=="Wall"):
                        elist.append(child)
                    elif(child.stage.game[l].__str__() =="Wall" and child.stage.game[d].__str__()=="Wall"):
                        elist.append(child)
                num+=1
        for child in childes:
            test=True
            if(child  not in elist):
                for i in positions:
                    if(child.stage.game[i].__str__() != "Box"):
                        test=False
                if(test==False):
                    q.put(child)
                else:
                    final=child
            if(final!=None):
                break
        if(final!=None):
            break
    if(final!=None):
        parent=final
        while(parent!=None):
            print(parent.action,end='<-')
            parent=parent.parent
    else:
        print("Failed")
    print()
    print("Congratulations")


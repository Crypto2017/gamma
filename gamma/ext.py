
            

class PathFinder():
    def __init__(self,matrix,dirs=8):
        self.matrix=matrix
        
        
    def neighbors(self,pos):
        neighbors=[]
        x,y=pos
        opt=[[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
        if self.dirs==8:
            opt.extend([[x+1,y+1],[x+1,y-1],[x-1,y-1],[x-1,y+1]])
        for option in opt:
            if self.exist(option):
                neighbors.append(self.get(option))
        return neighbors
        
    def get(self,pos):
        x,y=pos
        return [self.x,self.y,self.matrix[self.y][self.x]]
    
    def exist(self,pos):
        x,y=pos
        if y>=0 and x>=0 and y<= len(matrix) and y<=len(matrix[0]):
            return True
        return False
        
        
class Child():
    def __init__(sefl,parent,pos,path):
        self.parent=parent
        self.pos=pos
        self.path=path
        self.value=sum([val[2] for val in self.path])
        
        

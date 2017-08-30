import pickle
import os
import os.path

class Table():
    def __init__(self,path):
        self.path=path
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.num=0
        self.entries=[]
        self.load()
    def load(self):
        """Loads all entries from folder."""
        self.entries=[]
        files=[os.path.join(self.path,file) for file in os.listdir(self.path) if os.path.isfile(os.path.join(self.path,file))]
        for path in files:
            if path.endswith(".row"):
                inf=open(path,"rb")
                data=inf.read()
                inf.close()
                data=pickle.loads(data)
                data["__meta__"]["path"]=path
                self.entries.append(data)
            elif path.endswith(".cnfg"):
                inf=open(path,"rb")
                data=inf.read()
                inf.close()
                inf=pickle.loads(data)
                self.num=inf["num"]
        
    def where(self,cate,value):
        """All entries where entry[cate]==value. """
        for entry in self.entries:
            if entry[cate]==value:
                yield entry
                
    def where_any(self,value):
        """All entries where entry[any]==value"""
        for entry in self.entries:
            for cate in entry:
                if entry[cate]==value:
                    yield entry
                    break
    def get_all(self):
        """Returns all entries."""
        return self.entries
    def getAll(self):
        """Returns all entries."""
        return self.entries
                
    def search(self,value):
        """All entries where (value in entry[any])"""
        for entry in self.entries:
            for cate in entry:
                if str(value) in str(entry[cate]):
                    yield entry
                    break
                
    def query(self,*args,**kwargs):
        """example query(name="Max Mustermann",age=45) or query("and",type="article")"""
        q=[]
        for entry in self.entries:
            for key in kwargs:
                if entry[key]!=kwargs[key]:
                    break
            else:
                q.append(entry)
        for entry in q:
            vals=list(entry.values())
            for arg in args:
                if not self._check(arg,vals):
                    break
            else:
                yield entry
                
                
                
                
    def update(self,entry,**kwargs):
        """Updates entry, save complete Table."""
        entry.update(kwargs)
        self.dump()
        
    def _new(self,row):
        """Creates new entrie+file."""
        self._type(row)
        row["__meta__"]={}
        row["__meta__"]["path"]=os.path.join(self.path,str(self.num)+".row")
        self.entries.append(row)
        f=open(row["__meta__"]["path"],"wb")
        f.write(pickle.dumps(row))
        f.close()
        self.num+=1
        
    def new(self,row):
        """Creates new entrie+file, and save complete table."""
        self._new(row)
        self.dump()
        
    def dump(self):
        """Saves all entries."""
        for entry in self.entries:
            path=entry["__meta__"]["path"]
            dat=open(path,"wb")
            dat.write(pickle.dumps(entry))
            dat.close()
        f=open(os.path.join(self.path,"table.cnfg"),"wb")
        f.write(pickle.dumps({"num":self.num}))
        f.close()
        
    def clear(self):
        """Deletes all entries (file and virtual)."""
        for entry in self.entries:
            os.remove(entry["__meta__"]["path"])
        if os.path.exists(os.path.join(self.path,"table.cnfg")):
            os.remove(os.path.join(self.path,"table.cnfg"))
        self.num=0
        self.entries=[]
        
    def _check(self,key,args):
        """Check if any instance in args has key as substring."""
        key=str(key)
        for arg in args:
            if key in str(arg):
                return True
        return  False
    def _type(self,row):
        if type(row)==dict:
            for key in row:
                t=type(row[key])
                print(str(t))
                if t in [int,float,bool,list]:
                    continue
                elif t==dict:
                    self._type(row[key])
                else:
                    raise TypeError(str(type(t))+" isn't a valid type, use gamma.db.Pool for special Classes.")
        else:
            raise  TypeError(str(type(row))+" isn't a valid type, use gamma.db.Pool for special Classes.")
    
    def xml(self,gen):
        """Turns table into XML-String"""
        glob="<?xml version='1.0'?>\n"
        loc=""
        for entry in gen:
            for key in entry:
                if key!="__meta__":
                    loc+="\t\t<{}>{}</{}>\n".format(key,entry[key],key)
            glob+="\t<data>\n{}\t</data>\n".format(loc)
            loc=""
        return "<root>\n"+glob+"</root>"
    
    
class Pool():
    def __init__(self,path):
        self.path=path
        self.entries={}
        
    def load(self):
        """Load entries."""
        self.entries=[]
        files=[os.path.join((self.path,file),file) for file in os.listdir(self.path) if os.path.isfile(os.path.join(self.path,file))]
        for path,name in files:
            if path.endswith(".inf"):
                inf=open(path,"rb")
                data=inf.read()
                inf.close()
                data=pickle.loads(data)
                self.entries[name[:-4]]=data
                self.entries.append(data)
    def get(self,key):
        """Get entry."""
        return self.entries[key]
    def set(self,key,value):
        """Set entry."""
        self.entries[key]=value
        return self
    def get_all(self):
        """Returns all entries."""
        return self.entries
    def getAll(self):
        """Returns all entries."""
        return self.entries
    def dump(self):
        """Saves all entries."""
        for key in self.entries:
            entry=self.entries[key]
            path=os.path.join(self.path,key+".inf")
            dat=open(path,"wb")
            dat.write(pickle.dumps(entry))
            dat.close()
    def clear(self):
        """Deletes all entries (file and virtual)."""
        for name in self.entries:
            os.remove(os.path.join(self.path,str(name)+".inf"))
        self.entries={}
        
        
class DataBase():
    def __init__(self,path):
        self.path=path
        
    def getTable(self,name):
        """Returns Table if it exist already, otherwise creates a new one."""
        path=os.path.join(self.path,name)
        if not os.path.exists(path):
            os.mkdir(path)
        return Table(path)
        
    def getPool(self,name):
        """Returns Pool if it exist already, otherwise creates a new one."""
        path=os.path.join(self.path,name)
        if not os.path.exists(path):
            os.mkdir(path)
        return Pool(path)
    
    
        
    
    
        
            
            


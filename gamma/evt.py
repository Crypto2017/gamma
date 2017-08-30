
import pygame
#requires Gamma.reg(<obj>)



class Event(list):
    def __init__(*args):
        super().__init__()
        self.extend(list(args))
        
    def add(self,*funcs):
        """Binds *funcs to Event/Trigger/Signal"""
        self.extend(list(funcs))
        return self
    def __call__(self,func):
        """Binds func to Event/Trigger/Signal, use a decorator:   @trigger\ndef hi():\n\tprint("Hi!")"""
        self.append(func)
        return self
    def connect(self,evt):
        """Connects other Events/Triggers/Signals to Event/Trigger/Signal"""
        self.add(evt.action)
        return self
    def trigger(self):
        pass
    def emit(self):
        pass
    def action(self):
        pass


class Trigger(Event):
    
    def trigger(self):
        """Triggers trigger :)."""
        for func in self:
            func()
        return self
    def action(self):
        """Triggers trigger too."""
        self.trigger()
        return self

        
class Signal(Event):
    def __init__(self,value,*args):
        super().__init__(*args)
        self.value=value
        
    def getValue(self):
        """Returns last emiteted value."""
        return self.value

    def set(self,value):
        """Emits new value."""
        if value!=self.value:
            self.value=value
            self.emit()
        return self

    def emit(self):
        """Emits value."""
        for func in self:
            func(self.value)
        return self
    
    def action(self):
        """Emits value too."""
        self.emit()
        return self

            
class Controller():
    def __init__(self):
        pass
    
class KeyCtrl(Controller):
    def __init__(self,app,*keys):
        self.app=app
        self.app.reg(self)  #TODO: Add Gamma.reg too Gamma Class
        self.keys=list(keys)
        self.trigger=[Trigger() for k in keys]
        
    def update(self):
        """Updates Triggers"""
        kb=pygame.key.get_pressed()
        for i,key in enumerate(self.keys):
            if kb[key]:
                self.trigger[i].trigger()
                
#TODO: Arrow Controller

                
            
        
        
            
            

    
    
    

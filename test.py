from net import Client,Server,localhost

s=Server().bind((localhost(),90))

c=Client()
c.connect((localhost(),90))

s.listen()



    
    

    

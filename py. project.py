class tables:    
    def __init__(self ,num):
        self.n = num
    def start(self):
        for i in range(2, self.n + 1): 
            print("\n","TABLE OF",i,"\n")
            for j in range(1, 11):
                print(i,"i", j,"=",i*j) 
a=int(input("enter a value: ")) 
T=tables(a)
T.start()
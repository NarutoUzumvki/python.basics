class pen():

    def __init__(self,type,color):
        self.type=type
        self.color=color
pen1=pen('ballpoint','black')
print("Pen1 is of type " + pen1.type + " and its color is "+ pen1.color)


pen2=pen("Gel","Red")
print("Pen2 is of type " + pen2.type + " and its color is "+ pen2.color)
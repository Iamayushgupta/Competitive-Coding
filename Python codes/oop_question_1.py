class Line:
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    def distance(self):
        x1,y1=self.coor1
        x2,y2=self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    def slope(self):
        x1,y1=self.coor1
        x2,y2=self.coor2
        return (y2-y1)/(x2-x1)
c1=(3,2)
c2=(9,10)
line=Line(c1,c2)
print(line.distance())



class Cylinder():
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
    def volume(self):
        return 3.14*self.radius*self.radius*self.height
    def surface_area(self):
        return 2*3.14*self.radius*(self.height + self.radius)

cylinder=Cylinder(1,2)
print(cylinder.volume())

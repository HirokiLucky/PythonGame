from tkinter import*
from dataclasses import dataclass, field
@dataclass
class Maze:
    height: int=field(init=False, default=None)
    width: int=field(init=False, default=None)
    floormap: list=field(init=False, default=None)

    def set_floormap(self, height, width, floormap):
        self.width = width
        self.height = height
        self.floormap = floormap

   
    def from_file(self,filename):
        self.floormap = []
        with open(filename)as file:
            first_line = file.readline().rstrip("\n")
            point_non = first_line.split(",")
            self.height = int(point_non[0])
            self.width = int(point_non[1])
            
            for line in file:
                lines = line.rstrip("\n")
                points = lines.split(",")
                data = []
                for in_point in points:
                    data.append(int(in_point))
                self.floormap.append(data)
            if len(self.floormap) != self.height:
                raise Exception("mismatch map data (height)")
    
 

#迷路ゲーム
from tkinter import*
from dataclasses import dataclass, field
from maze import Maze

@dataclass
class MazeGame:
    maze: Maze = field(init = False, default = None)
    player: tuple=field(init = False, default = None)

    def draw_floormap(self):
        n = 0
        m = 0
        for x in range(self.maze.height):
            for y in range(self.maze.width):
                canvas.create_rectangle(100 * y + 50, 100 * x + 50,
                                100 * (y + 1) + 50, 100 * (x + 1) + 50,outline = "black")
                
        for a in self.maze.floormap:
            for b in a:
                if (b == 1):
                    canvas.create_rectangle(100 * n + 50, 100 * m + 50,
                                100 * (n + 1) + 50, 100 * (m + 1) + 50,fill = "black")
                    canvas.create_text(100 * (n) + 100, 100 * (m) + 100, text = b, font = ("Helvetica", 30))
                    n = n + 1
                elif (b == 0):
                    canvas.create_rectangle(100 * n + 50, 100 * m + 50,
                                100 * (n + 1) + 50, 100 * (m + 1) + 50,fill = "blue")
                    n = n + 1
                elif (b == 8):
                    canvas.create_rectangle(100 * n + 50, 100 * m + 50,
                                100 * (n + 1) + 50, 100 * (m + 1) + 50,fill = "red")
                    canvas.create_text(100 * (n) + 100, 100 * (m) + 100, text = b, font = ("Helvetica", 30))
                    n = n + 1
                elif (b == 9):
                    canvas.create_rectangle(100 * n + 50, 100 * m + 50,
                                100 * (n + 1) + 50, 100 * (m + 1) + 50,fill = "yellow")
                    canvas.create_text(100 * (n) + 100, 100 * (m) + 100, text = b, font = ("Helvetica", 30))
                    n = n + 1
                elif (b == 3):
                    canvas.create_rectangle(100 * n + 50, 100 * m + 50,
                                100 * (n + 1) + 50, 100 * (m + 1) + 50,fill = "orange")
                    n = n + 1
            m = m + 1
            n = 0

    def set_player(self, i, j):
        self.player = (i, j)

    def set_goal(self, i, j):
        self.goal = (i, j)

    def draw_player(self):
        canvas.create_rectangle(100 * self.player[1] + 80, 100 * self.player[0] + 80,
                                100 * self.player[1] + 120, 100 * self.player[0] + 120, fill = "cyan")
        if (self.maze.floormap[self.player[0]][self.player[1]] == 9):       
            canvas.delete("all")
            canvas.create_rectangle(0,0,1500, 1500, fill="black")
            canvas.create_text(500, 500, text = "Game over", font = ("Helvetica", 50), fill = "white")
            exit = False
        
        
    def redraw(self):
        canvas.delete("all")
        #print(self.player[0], self.player[1])
        self.draw_floormap()
        self.draw_player()

    def player_up(self, event):
        if (self.maze.floormap[self.player[0] - 1][self.player[1]] != 1):
            self.set_player(self.player[0] - 1, self.player[1])
            self.maze.floormap[self.player[0] + 1][self.player[1]] = 3

    def player_down(self, event):
        if (self.maze.floormap[self.player[0] + 1][self.player[1]] != 1):
            self.set_player(self.player[0] + 1, self.player[1])
            self.maze.floormap[self.player[0] - 1][self.player[1]] = 3

    def player_right(self, event):
        if (self.maze.floormap[self.player[0]][self.player[1] + 1] != 1):
            self.set_player(self.player[0], self.player[1] + 1)
            self.maze.floormap[self.player[0]][self.player[1] - 1] = 3

    def player_left(self, event):
        if (self.maze.floormap[self.player[0]][self.player[1] - 1] != 1):
            self.set_player(self.player[0], self.player[1] - 1)
            self.maze.floormap[self.player[0]][self.player[1] + 1] = 3
        

    def start(self):
        self.maze = Maze()
        #self.set_floormap = self.maze.set_floormap()
        self.from_file = self.maze.from_file(r"map.txt")
        canvas.bind_all('<KeyPress-Up>', self.player_up)
        canvas.bind_all('<KeyPress-Down>', self.player_down)
        canvas.bind_all('<KeyPress-Right>', self.player_right)
        canvas.bind_all('<KeyPress-Left>', self.player_left)

        x = 0
        for a in self.maze.floormap:
            y = 0
            for b in a:
                if (b == 8):
                    self.set_player(x, y)
                if (b == 9):
                    self.set_goal(x, y)
                y = y + 1
            x = x + 1
        self.redraw()
        print(self.player[0], self.player[1])
        print(self.maze.floormap)
        
tk = Tk()
canvas = Canvas(tk,width = 1500, height = 1500)
canvas.pack()
game = MazeGame()
game.start()

while True:
    game.redraw()
    tk.update()
tk.mainloop()
  


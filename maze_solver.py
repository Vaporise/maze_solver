from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(master=self.__root,width=width,height=height)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    
    def wait_for_close(self):
        self.__running = True
        while self.__running = True:
            self.redraw() 

    
    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)
    

def main():
        win = Window(800, 600)
        win.wait_for_close()    

if __name__ == "__main__":
     main()


class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1 , point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas , fill_color="black"):
        canvas.create_line(
            self.point1.x, self.point1.y, #first point co-ords
             self.point2.x, self.point2.y, #second points co-ords
            fill=fill_color, width=2
        )

    

    


from maze_solver import Window, Line, Point

def main():
        win = Window(800, 600)

        top_left = Point(100, 100)
        top_right = Point(200, 100) 
        bottom_right = Point(200, 300)
        bottom_left = Point(100, 300)

        line1 = Line(top_left, top_right)
        line2 = Line(top_right, bottom_right)
        line3 = Line(bottom_right, bottom_left)
        line4 = Line(bottom_left, top_left)

        win.draw_line(line1, "black")
        win.draw_line(line2, "blue")
        win.draw_line(line3, "red")
        win.draw_line(line4, "purple")

        win.wait_for_close()    

if __name__ == "__main__":
     main()
import tkinter as tk

CELL_SIZE = 20
GRID_WIDTH = 20
GRID_HEIGHT = 20
ERASER_SIZE = 40

class EraserCanvasApp:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=GRID_WIDTH * CELL_SIZE, height=GRID_HEIGHT * CELL_SIZE)
        self.canvas.pack()

        self.cells = []
        for row in range(GRID_HEIGHT):
            cell_row = []
            for col in range(GRID_WIDTH):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='white')
                cell_row.append(rect)
            self.cells.append(cell_row)

        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, outline='black')

        self.canvas.bind("<B1-Motion>", self.move_eraser)

    def move_eraser(self, event):
        x1 = event.x - ERASER_SIZE // 2
        y1 = event.y - ERASER_SIZE // 2
        x2 = event.x + ERASER_SIZE // 2
        y2 = event.y + ERASER_SIZE // 2

        self.canvas.coords(self.eraser, x1, y1, x2, y2)

        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                cell = self.cells[row][col]
                cx1, cy1, cx2, cy2 = self.canvas.coords(cell)

                if not (cx2 < x1 or cx1 > x2 or cy2 < y1 or cy1 > y2):
                    self.canvas.itemconfig(cell, fill='white')

def main():
    root = tk.Tk()
    root.title("Eraser Canvas")
    app = EraserCanvasApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

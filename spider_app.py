import math
import tkinter as tk


class SpiderChart(tk.Canvas):
    """a canvas that displays datapoints as a SpiderChart
    """
    width=500
    height=500
    def __init__(self, master, datapoints, concentrics=10, scale=200):
        super().__init__(master, width=self.width, height=self.height)
        self.scale = scale
        self.center = self.width // 2, self.height // 2
        self.labels = tuple(d[0] for d in datapoints)
        self.values = tuple(d[1] for d in datapoints)
        self.num_pts = len(self.labels)
        self.concentrics = [n/(concentrics) for n in range(1, concentrics + 1)]
        self.draw()
        
    def position(self, x, y):
        """use +Y pointing up, and origin at center
        """
        cx, cy = self.center
        return x + cx, cy - y
    
    def draw_circle_from_radius_center(self, radius):
        rad = radius * self.scale
        x0, y0 =  self.position(-rad, rad)
        x1, y1 =  self.position(rad, -rad)
        return self.create_oval(x0, y0, x1, y1, dash=(1, 3))
    
    def draw_label(self, idx, label):
        angle = idx * (2 * math.pi) / self.num_pts
        d = self.concentrics[-1] * self.scale
        x, y = d * math.cos(angle), d * math.sin(angle)
        self.create_line(*self.center, *self.position(x, y), dash=(1, 3))
        d *= 1.1 
        x, y = d * math.cos(angle), d * math.sin(angle)
        self.create_text(*self.position(x, y), text=label)
        
    def draw_polygon(self):
        points = []
        for idx, val in enumerate(self.values):
            d = (val / 100) * self.scale
            angle = idx * (2 * math.pi) / self.num_pts
            x, y = d * math.cos(angle), d * math.sin(angle)
            points.append(self.position(x, y))
        self.create_polygon(points, fill='cyan')
        
    def draw(self):
        self.draw_polygon()
        for concentric in self.concentrics:
            self.draw_circle_from_radius_center(concentric)
        for idx, label in enumerate(self.labels):
            self.draw_label(idx, label)
        
            
data = [('stamina', 70), ('python-skill', 100), ('strength', 80), ('break-dance', 66), ('speed', 45), ('health', 72), ('healing', 90), ('energy', 12), ('libido', 100)]

root = tk.Tk()
spider = SpiderChart(root, data)
spider.pack(expand=True, fill=tk.BOTH)

root.mainloop()
        
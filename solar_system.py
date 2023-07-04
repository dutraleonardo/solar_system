import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta

class Object:
    
    def __init__(self, name, rad, color, r, v):
        self.name = name
        self.r    = np.array(r, dtype=float)
        self.v    = np.array(v, dtype=float)
        self.xs = []
        self.ys = []
        self.plot = plt.scatter(r[0], r[1], color=color, s=rad**2, edgecolors=None, zorder=10)
        self.line, = plt.plot([], [], color=color, linewidth=1.4)

class SolarSystem:
    
    def __init__(self, thesun):
        self.thesun = thesun
        self.planets = []
        self.time = None
        self.timestamp = plt.text(.03, .94, 'Date: ', color='w', transform=plt.gca().transAxes, fontsize='x-large')
    
    def add_planet(self, planet):
        self.planets.append(planet)
    
    def evolve(self):
        dt = 1
        self.time += timedelta(dt)
        plots = []
        lines = []

        for i, p in enumerate(self.planets):
            p.r += p.v * dt
            acc = -2.959e-4 * p.r / np.sum(p.r**2)**(3./2)
            p.v += acc * dt
            p.xs.append(p.r[0])
            p.ys.append(p.r[1])
            p.plot.set_offsets(p.r[:2])
            plots.append(p.plot)
            p.line.set_xdata(p.xs)
            p.line.set_ydata(p.ys)
            lines.append(p.line)
        
        if len(p.xs) > 10000:
            raise SystemExit("ATENÇÃO! O programanda está sendo pausadopara evitar sobrecarga de memória.")
        
        self.timestamp.set_text('Date: {}'.format(self.time.isoformat()))
        
        return plots + lines + [self.timestamp]
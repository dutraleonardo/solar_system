#!/usr/bin/env python
import json
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime
from solar_system import SolarSystem, Object


def main():
    matplotlib.use('qtagg')
    fig = plt.figure(figsize=[6, 6])
    ax = plt.axes([0., 0., 1., 1.], xlim=(-1.8, 1.8), ylim=(-1.8, 1.8))
    ax.set_aspect('equal')
    ax.axis('off')

    # carrega plano de fundo
    img = plt.imread("ceu.jpg")

    # carrega as configs
    with open("config.json", 'r') as f:
        planets = json.load(f)
    
    system = SolarSystem(Object("Sun", 28, 'yellow', [0, 0, 0], [0, 0, 0]))
    system.time = datetime.strptime(planets["date"], '%d-%m-%Y').date()
    
    colors = [plt.get_cmap('Paired')(i) for i in [0, 4, 2, 7]]
    texty = [.47, .73, 1, 1.5]
    
    for i, nasaid in enumerate([1, 2, 3, 4]):
        planet = planets[str(nasaid)]
        system.add_planet(Object(nasaid, 20 * planet["size"], colors[i], planet["r"], planet["v"]))
        ax.text(0, - (texty[i] + 0.1), planet["name"], color=colors[i], zorder=1000, ha='center', fontsize='large')
    
    def animate(i):
        return system.evolve()

    duration = 2 * 365 # dois anos
    
    ani = animation.FuncAnimation(fig, animate, repeat=False, frames=duration, blit=True, interval=20,)

    plt.imshow(img, extent=[-2, 2, -2, 2], aspect='auto')
    
    plt.show()

main()

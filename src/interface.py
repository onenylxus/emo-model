# Import
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm


# Interface class
class Interface:
  # Constructor
  def __init__(self, opt, name, folder):
    self.opt = opt          # Optimizer
    self.name = name        # Model name
    self.folder = folder    # Folder name

    self.positions = []     # Position records
    self.values = []        # Value records
    self.bestPositions = [] # Solution positons
    self.bestValues = []    # Solution values

    self.dirb = True        # Directory boolean

    # Create missing directories
    if self.dirb:
      if not os.path.exists(f'{os.getcwd()}/output'):
        os.mkdir(f'{os.getcwd()}/output')
        print('Output folder created')
      if not os.path.exists(f'{os.getcwd()}/output/{self.folder}'):
        os.mkdir(f'{os.getcwd()}/output/{self.folder}')
        print(f'{self.folder} folder created in output folder')
      print('')
    self.dirb = False

    # Print interface header
    print('Electromagnetism-like Optimization Model')
    print(f'Model: {self.name}\n')
    self.record()

  # Record
  def record(self):
    self.positions.append(self.opt.population.positions())
    self.values.append(self.opt.population.values())
    self.bestPositions.append([v for v in self.opt.solution().pos])
    self.bestValues.append(self.opt.solution().value())

    l = len(self.bestValues) - 1
    print(f'Generation {l}:')
    for i in range(self.opt.size):
      print(f'  Particle {i + 1}: {self.positions[l][i]}, value = {self.values[l][i]}')
    print(f'  Best particle is particle {self.opt.solution().index + 1} with value {self.bestValues[l]}\n')

  # Plot objective function value
  def plot_ofv(self):
    plt.plot(self.bestValues, linewidth=4)
    plt.grid()
    plt.xlabel('Generations')
    plt.ylabel('Objective function minimum')
    plt.savefig('output/%s/ofv.png' %(self.folder), format='png')
    plt.clf()

  # Plot contour
  def plot_contour(self, f):
    if self.opt.dim == 2:
      xr = np.linspace(self.opt.lower[0], self.opt.upper[0], 50)
      yr = np.linspace(self.opt.lower[1], self.opt.upper[1], 50)
      X, Y = np.meshgrid(xr, yr)
      Z = f(X, Y)

      plt.contour(X, Y, Z, linewidths=2)
      if self.opt.gen > 0:
        plt.plot(self.bestPositions[self.opt.gen - 1][0], self.bestPositions[self.opt.gen - 1][1], 'yo')
      plt.scatter(self.positions[self.opt.gen][:, 0], self.positions[self.opt.gen][:, 1], marker='x')
      plt.plot(self.opt.solution().pos[0], self.opt.solution().pos[1], 'ro')
      plt.title(f'Generation {self.opt.gen} (ofv={self.bestValues[self.opt.gen]})')
      plt.xlim(self.opt.lower[0], self.opt.upper[0])
      plt.ylim(self.opt.lower[1], self.opt.upper[1])
      plt.savefig('output/%s/contour_iter%03d.png' %(self.folder, self.opt.gen), format='png')
      plt.clf()

  # Plot contour with colourful particles
  def plot_contour_cm(self, f):
    if self.opt.dim == 2:
      c = cm.rainbow(np.linspace(0, 1, self.opt.size))
      xr = np.linspace(self.opt.lower[0], self.opt.upper[0], 50)
      yr = np.linspace(self.opt.lower[1], self.opt.upper[1], 50)
      X, Y = np.meshgrid(xr, yr)
      Z = f(X, Y)

      plt.contour(X, Y, Z, linewidths=2)
      plt.scatter(self.positions[self.opt.gen][:, 0], self.positions[self.opt.gen][:, 1], marker='x', color=c)
      plt.plot(self.opt.solution().pos[0], self.opt.solution().pos[1], 'o')
      plt.title(f'Generation {self.opt.gen} (ofv={self.bestValues[self.opt.gen]})')
      plt.xlim(self.opt.lower[0], self.opt.upper[0])
      plt.ylim(self.opt.lower[1], self.opt.upper[1])
      plt.savefig('output/%s/contour_iter%03d.png' %(self.folder, self.opt.gen), format='png')
      plt.clf()

  # Plot position bar chart
  def plot_posbar(self):
    for k in range(self.opt.dim):
      plt.bar(k, self.opt.solution().pos[k])
    plt.title(f'Generation {self.opt.gen} (ofv={self.bestValues[self.opt.gen]})')
    plt.ylabel('Values')
    plt.savefig('output/%s/bar_iter%03d.png' %(self.folder, self.opt.gen), format='png')
    plt.clf()

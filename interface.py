# Import
import numpy as np
import os
import matplotlib.pyplot as plt


# Interface class
class Interface:
  # Constructor
  def __init__(self, opt, name, folder):
    self.opt = opt       # Optimizer
    self.name = name     # Model name
    self.folder = folder # Folder name

    self.positions = []  # Position records
    self.values = []     # Value records
    self.trend = []      # Solution trend

    self.dirb = True     # Directory boolean

    # Create missing directories
    if self.dirb:
      if not os.path.exists(f'{os.getcwd()}/contours'):
        os.mkdir(f'{os.getcwd()}/contours')
        print('Contour folder created')
      if not os.path.exists(f'{os.getcwd()}/contours/{self.folder}'):
        os.mkdir(f'{os.getcwd()}/contours/{self.folder}')
        print(f'{self.folder} folder created in contour folder')
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
    self.trend.append(self.opt.solution().value())

    l = len(self.trend) - 1
    print(f'Iteration {l}:')
    for i in range(self.opt.size):
      print(f'  Particle {i + 1}: {self.positions[l][i]}, value = {self.values[l][i]}')
    print(f'  Best particle is particle {self.opt.solution().index + 1} with value {self.trend[l]}\n')

  # Plot objective function value
  def plot_ofv(self):
    plt.figure()
    plt.plot(self.trend, linewidth=4)
    plt.grid()
    plt.xlabel('Iterations')
    plt.ylabel('Objective function minimum')
    plt.show()
    plt.savefig('contours/%s/ofv.png' %(self.folder), format='png')
    plt.clf()

  # Plot contour
  def plot_contour(self, f):
    if self.opt.dim == 2:
      xr = np.linspace(self.opt.lower[0], self.opt.upper[0], 50)
      yr = np.linspace(self.opt.lower[1], self.opt.upper[1], 50)
      X, Y = np.meshgrid(xr, yr)
      Z = f(X, Y)

      plt.figure()
      plt.contour(X, Y, Z, linewidths=2)
      plt.scatter(self.positions[self.opt.iter][:, 0], self.positions[self.opt.iter][:, 1], marker='x')
      plt.plot(self.opt.solution().pos[0], self.opt.solution().pos[1], 'ro')
      plt.title(f'Iteration {self.opt.iter}')
      plt.xlim(self.opt.lower[0], self.opt.upper[0])
      plt.ylim(self.opt.lower[1], self.opt.upper[1])
      plt.show()
      plt.savefig('contours/%s/iter%03d.png' %(self.folder, self.opt.iter), format='png')
      plt.clf()

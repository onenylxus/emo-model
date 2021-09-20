# Import
import matplotlib.pyplot as plt

# Interface class
class Interface:
  # Constructor
  def __init__(self, opt):
    self.opt = opt      # Optimizer

    self.positions = [] # Position records
    self.values = []    # Value records
    self.trend = []     # Solution trend

    # Print interface header
    print('Electromagnetism-like Optimization Model')
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
    print(f'  Best particle is particle {self.opt.population.best().index + 1} with value {self.trend[l]}')

  # Plot objective function value
  def plot_ofv(self):
    plt.figure()
    plt.plot(self.trend, linewidth=2)
    plt.grid()
    plt.xlabel('Iterations')
    plt.ylabel('Objective function minimum')

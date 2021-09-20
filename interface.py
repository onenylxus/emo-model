# Import
import matplotlib.pyplot as plt
from optimizer import Optimizer

# Interface class
class Interface:
  # Constructor
  def __init__(self, opt):
    self.opt = opt                     # Optimizer

    self.trend = [self.opt.solution()] # Solution trend

    # Print interface header 
    print('Electromagnetism-like Optimization Model')

  # Record
  def record(self):
    self.trend.append(self.opt.solution())
    # print(f'Solution update: {self.opt.solution().value}')

  # Plot objective function value
  def plot_ofv(self):
    plt.figure()
    plt.plot([v.value for v in self.trend],linewidth=2)
    plt.grid()
    plt.xlabel('Iterations')
    plt.ylabel('Objective function minimum')

# Import
import numpy as np
from population import Population

# Constants
MAX_LSITER = 50
STEP_SIZE = 0.001
LS_MODE = 1

# Optimizer class
class Optimizer:
  # Constructor
  def __init__(self, dim, lower, upper, size, f, lsiter=None, step=None, lsmode=None):
    # Space definition
    self.dim = dim                                             # Dimension of the space
    self.lower = np.array(lower)                               # Lower bound of the space
    self.upper = np.array(upper)                               # Upper bound of the space
    self.size = size                                           # Number of particles
    self.f = f                                                 # Objective function

    # Limits
    self.lsiter = lsiter if lsiter is not None else MAX_LSITER # Maximum number of local search iterations
    self.step = step if step is not None else STEP_SIZE        # Step size
    self.lsmode = lsmode if lsmode is not None else LS_MODE    # Best particle for local search

    # Data
    self.gen = 0                                               # Number of generations
    self.population = Population(self)                         # Population

  # Iterate
  def iterate(self):
    self.population.iterate()
    self.gen += 1

  # Get solution
  def solution(self):
    return self.population.best()

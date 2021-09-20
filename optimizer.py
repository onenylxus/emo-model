# Import
import numpy as np
from population import Population

# Constants
MAX_ITERATIONS = 50
STEP_SIZE = 0.001
RANDOM_SEED = 12345


# Optimizer class
class Optimizer:
  # Constructor
  def __init__(self, data):
    # Space definition
    self.dim = data.dim                                                      # Dimension of the space
    self.lower = np.array(data.lower)                                        # Lower bound of the space
    self.upper = np.array(data.upper)                                        # Upper bound of the space
    self.size = data.size                                                    # Number of particles
    self.f = data.f                                                          # Objective function

    # Limits
    self.lsiter = self.lsiter if self.lsiter is not None else MAX_ITERATIONS # Maximum number of local search iterations
    self.seed = self.seed if self.seed is not None else RANDOM_SEED          # Random number generator seed
    self.step = self.step if self.step is not None else STEP_SIZE            # Step size

    # Data
    self.iter = 0                                                            # Number of iterations
    self.population = Population(self)                                       # Population

  # Iterate
  def iterate(self):
    self.population.iterate()
    self.iter += 1

  # Get solution
  def solution(self):
    return self.population.best_position()

# Import
import numpy as np

# Particle class
class Particle:
  # Constructor
  def __init__(self, parent, index, pos=None):
    self.parent = parent # Parent (Population)
    self.index = index   # Index
    self.pos = pos       # Position
    self.value = 0       # Objective function value

    # Initialize position
    if self.pos is None:
      self.pos = np.zeros(self.opt().dim)
      for k in range(self.opt().dim):
        lmd = self.rng()
        self.pos[k] = self.opt().lower[k] + lmd * (self.opt().upper[k] - self.opt().lower[k])
    
    # Initial evaluation
    self.eval()

  # Search function
  def search(self):
    count = 1
    length = self.opt().step * self.parent.max_range()
    for i in range(self.opt().size):
      for k in range(self.opt().dim):
        lmd1 = self.rng()
        while count < self.opt().lsiter:
          y = self.copy(self.parent.particles[i].pos)
          lmd2 = self.rng()

          if lmd1 > 0.5:
            y[k] = np.minimum(y[k] + lmd2 * length, self.opt().upper[k])
          else:
            y[k] = np.maximum(y[k] - lmd2 * length, self.opt().lower[k])

          if self.opt().f(y) < self.opt().f(self.parent.particles[i].pos):
            self.parent.particles[i].pos = self.copy(y)
            count = self.opt().lsiter - 1
          count += 1

  # Movement
  def move(self):
    for i in range(self.opt().size):
      if i is not self.parent.best().index:
        lmd = self.rng()
        f = self.parent.forces()[i] / np.sqrt(np.dot(self.parent.forces()[i], self.parent.forces()[i]))

        for k in range(self.opt().dim):
          if f[k] > 0:
            self.pos[k] += lmd * f[k] * (self.opt().upper[k] - self.pos[k])
          else:
            self.pos[k] += lmd * f[k] * (self.pos[k] - self.opt().lower[k])
            
            
  # Get optimizer
  def opt(self):
    return self.parent.parent

  # Copy function
  def copy(self, pos):
    return np.array([v for v in pos])
    
  # Evaluate function
  def eval(self):
    self.value = self.opt().f(self.pos)

  # Random number generator
  def rng(self):
    return np.random.uniform()

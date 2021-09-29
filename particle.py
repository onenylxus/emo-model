# Import
import numpy as np

# Particle class
class Particle:
  # Constructor
  def __init__(self, parent, index, pos=None):
    self.parent = parent # Parent (Population)
    self.index = index   # Index
    self.pos = pos       # Position

    # Initialize position
    if self.pos is None:
      self.pos = np.zeros(self.opt().dim)
      for k in range(self.opt().dim):
        lmd = self.rng()
        self.pos[k] = self.opt().lower[k] + lmd * (self.opt().upper[k] - self.opt().lower[k])

  # Search function
  def search(self):
    count = 1
    length = self.opt().step * self.parent.max_range()
    for k in range(self.opt().dim):
      lmd1 = self.rng()
      while count < self.opt().lsiter:
        y = self.copy(self.pos)
        lmd2 = self.rng()

        if lmd1 > 0.5:
          y[k] += lmd2 * length
        else:
          y[k] -= lmd2 * length

        if self.opt().f(y) < self.value():
          self.pos = self.copy(y)
          count = self.opt().lsiter - 1
        count += 1

    print('Search done')

  # Movement
  def move(self):
    if self.index is not self.parent.best().index:
      for i in range(self.opt().size):
        if i is not self.index:
          lmd = self.rng()
          t = self.parent.tfv[i]
          f = t / np.sqrt(np.dot(t, t))

          for k in range(self.opt().dim):
            if f[k] > 0:
              self.pos[k] += lmd * f[k] * (self.opt().upper[k] - self.pos[k])
            else:
              self.pos[k] += lmd * f[k] * (self.pos[k] - self.opt().lower[k])

    print(f'Particle {self.index} move done')


  # Get optimizer
  def opt(self):
    return self.parent.parent

  # Get value
  def value(self):
    return self.opt().f(self.pos)

  # Copy function
  def copy(self, pos):
    return np.array([v for v in pos])

  # Random number generator
  def rng(self):
    return np.random.uniform()

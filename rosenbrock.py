# Import
from interface import Interface
from optimizer import Optimizer

# Rosenbrock function as objective function
def rosenbrock(pos):
  return (1 - pos[0]) ** 2 + 100 * ((pos[1] - pos[0] ** 2) ** 2)

def rosenbrockV(x, y):
  return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2

# Execution script
if __name__ == '__main__':
  o = Optimizer(2, [-2, -2], [2, 2], 10, rosenbrock)
  i = Interface(o, 'Rosenbrock function', 'rosenbrock')
  i.plot_contour(rosenbrockV)

  while i.opt.gen < 50:
    i.opt.iterate()
    i.record()
    i.plot_contour(rosenbrockV)
  i.plot_ofv()

# Import
from interface import Interface
from optimizer import Optimizer

# Rosenbrock function as objective function
def rosenbrock(pos):
    return (1 - pos[0]) ** 2 + 100 * ((pos[1] - pos[0] ** 2) ** 2)


# Execution script
if __name__ == '__main__':
    o = Optimizer(2, [-2, -2], [2, 2], 10, rosenbrock, None, None)
    i = Interface(o)

    while i.opt.iter < 100:
      i.opt.iterate()
      i.record()
    i.plot_ofv()

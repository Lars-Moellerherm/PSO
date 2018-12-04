from pso import pso
from example_objectives import objective
import numpy as np

Problem = 1

V, l_bound, u_bound, f, constr = objective(Problem)

P = pso(V,l_bound,u_bound,f,constraints=constr,c=2.13,s=1.05,w=0.41,pop=100,integer=True)
P.plot()
P.moving(1)
P.plot()
Pareto_Front = P.get_solution()
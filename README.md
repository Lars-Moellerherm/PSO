# PSO
single- and multi-objective **Particle Swarm Optimizer**

This module can optimize single and multi objective problems.
It uses [**non domination sorting**](https://www.iitk.ac.in/kangal/Deb_NSGA-II.pdf)[1] for multi objective problems.

## Particle Swarm Optimization Algorithm

The [Particle Swarm Optimizer](https://en.wikipedia.org/wiki/Particle_swarm_optimization) is an Algorithm which iteratively searches for the optimal solution in a search space, according to a fitness evaluation. The swarm consists of a number of particles, which are solutions in the search space. These particles move in each step, depending on the velocity. The velocity depends on the actual distance of the particle to the best position in history of the particle and to the globally best known position.

Because PSO is an metaheuristic there is no garantee that the swarm moves to the global optimum and doesn't get stuck in a local Extremum

## How to use pso class:

### Initiate :
                    
- **_att_** : number off Attributes
                        
- **_l_b_** : lower bounds for every Attribute (sticks to these bounds) (numpy.array with length *att*)

- **_u_b_** : upper bounds for every Attribute (sticks to these bounds) (numpy.array with length *att*)
                        
- **_obj_func_** : objective function/s (for multi objective use list of function handels)
                        
- **_constraints_** : constraint function/s from type penalty (default: empty list)
                        
- **_c_** : cognitive parameter (default : *2.1304*)
                        
- **_s_** : sozial parameter (default : *1.0575*)
                        
- **_w_** : inertia (default : *0.4091*)
                        
- **_pop_** : size of population (default : *156*)
                        
- **_vm_** : max velocity for every attribute (default: *u_b - l_b*)
                        
- **_integer_** : Integer constraint for every attribute (default *False*)
	
### Functions :
        
- **_moving(steps, time_termination = -1)_** : 	
  - doing *steps* iterations
  - if *timer_termination != -1* terminates before *steps* or done if *time > time_termination*
                	
- **_plot(best_p=True, x_coord = 0, y_coord = 1)_** : plotting the actual swarm
  - *best_p = True* or *False* -> want to plot the personal best or the actual position of all particles
  - *x_coord = 0,1,...* -> for single: which position variable should be plotted ; for multi: which objective value should be plotted on the y-axis
  - *y_coord = 0,1,...* -> for single: not relevant ; for multi: which objective value should be plottet on the y-axis
                
- **_get_solution(whole_particle = True)_** : single -> returns global best particle ; multi -> returns Pareto Front
  - *whole_particle = True* or *False* -> returns particle class or just the objective value	   

## Missing for now:

- Termination Criterium


1. Kalyanmoy Deb, Amrit Pratap, Sameer Agarwal, and T. Meyarivan, A Fast Elitist Multiobjective Genetic Algorithm: NSGA-II, IEEE Transactions on Evolutionary Computation 6 (2002), no. 2, 182 – 197. 

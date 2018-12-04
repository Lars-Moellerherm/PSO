# PSO
single- and multi-objective particle swarm Optimizer

This module can optimize single and multi objective Problems.

How to use pso class:

	Initiate the class pso:
                    
			att: number off Attributes
                        
			l_b: lower bounds for every Attribute (numpy.array with length att)
                        
			u_b: upper bounds for every Attribute (numpy.array with length att)
                        
			obj_func: objective function/s (for multi objective use list of function handels)
                        
			constraints: constraint function/s from type penalty (default: empty list)
                        
			c: cognitive parameter (default:2.1304)
                        
			s: sozial parameter (default:1.0575)
                        
			w: inertia (default:0.4091)
                        
			pop: size of population (default:156)
                        
			vm: max velocity for every attribute (default: upper bound - lower bound)
                        
			integer: Integer constraint for every attribute (default False)
	
	Functions:
        
		moving(steps): doing steps iterations
                
		plot(): plotting the actual swarm
                
		get_solution(whole_particle=True): whole_particle=      -True returns the solution as type(particle class);
                
                                                                        -False returns just the objective Value/s
						
				-single: The global best particle
                                
				-multi: The Pareto Front		   

Missing for now:

	Termination Criterium

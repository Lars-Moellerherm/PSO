import random
import matplotlib.pyplot as plt
import numpy as np


class particle_single():
    '''
    att -> number of Attributes
    position -> Particle attribute values
    velocity -> particle velocity it has been moved with
    best_p -> best particle in the past gets just set by first_set_best
    obj_function -> objective functions
    constraints -> constraints
    obj_value -> objective values
    '''
    
    def __init__(self,obj_func,attribute_number,constr=[],vmax=np.array(np.nan),l_bound=np.array(np.nan),u_bound=np.array(np.nan),integer=np.array(np.nan),position=np.array(np.nan),velocity=np.array(np.nan)):
        self.obj_function = obj_func
        if type(constr)!=list:
            constr = [constr]
        self.constraints = constr
        self.att = attribute_number
        if np.all(np.isnan(position))==False:
            self.position = position
        else:
            try:
                if attribute_number!=1:
                    init_pos = []
                    for i in range(self.att):
                        if integer[i]==False:
                            init_pos.append(random.uniform(l_bound[i],u_bound[i]))
                        else:
                            init_pos.append(random.randint(l_bound[i],u_bound[i]))
                    self.position = np.array(init_pos)
                else:
                    if integer==False:
                        self.position= random.uniform(l_bound,u_bound)
                    else:
                        self.position= random.randint(l_bound,u_bound)
            except:
                print('We need lower and upper bound for init position')
        
        self.obj_value = self.calc_obj_value()
        if np.all(np.isnan(velocity))==False:
            self.velocity = velocity
        else:
            try:
                if attribute_number!=1:
                    self.velocity = np.array([random.uniform(-vmax[i],vmax[i]) for i in range(self.att)])
                else:
                    self.velocity = random.uniform(-vmax,vmax)
            except:
                print('we need an vmax for init velocity')
        self.best_p=np.nan
        
    def __repr__(self):
        return f"Single objective particle with: \n\t position {self.position} \n\t velocity {self.velocity} \n\t objective value {self.obj_value}"
        
    def set_position(self,new_pos):
        self.position = new_pos
        self.obj_value = self.calc_obj_value()
        
    def set_velocity(self,new_v):
        self.velocity = new_v
        
    def get_obj_value(self):
        return self.obj_value
    
    def init_p_best(self):
        self.best_p = particle_single(self.obj_function,self.att,constr=self.constraints,position=self.position,velocity=self.velocity)
        
    def compare_p_best(self):
        if self.obj_value<self.best_p.obj_value:
            self.best_p.set_position(self.position)
        
    def compare(self,part2):
        return self.obj_value<part2.obj_value
        
    def plot(self, best_p, x_coord, y_coord):
        if best_p:
            plt.plot(self.best_p.position[x_coord],self.best_p.obj_value,'k.')
        else:
            plt.plot(self.position[x_coord],self.obj_value,'k.')
        
    def calc_obj_value(self):
        if not self.constraints:
            return self.obj_function(self.position)
        else:
            penalty = sum([con(self.position) for con in self.constraints])
            return self.obj_function(self.position) + penalty
    
  
    
    
class particle_multi(particle_single):
    '''
    att -> number of attributes
    position -> Particle attribute values
    velocity -> particle velocity it has been moved with
    best_p -> best particle in the past gets just set by first_set_best
    obj_functions -> objective functions
    constraints -> canstraint functions
    obj_values -> objective values
    S -> particles this particle dominates
    n -> number of particles this particle is dominated by
    distance -> crowding distance
    rank -> domination rank
    '''
    
    def __init__(self,obj_func,attribute_number,constr=[],vmax=np.array(np.nan),l_bound=np.array(np.nan),u_bound=np.array(np.nan),integer=np.array(np.nan),position=np.array(np.nan),velocity=np.array(np.nan)):
        self.obj_functions = obj_func
        self.constraints=constr
        self.att = attribute_number
        if np.all(np.isnan(position))==False:
            self.position=position
        else:
            try:
                if attribute_number!=1:
                    init_pos = []
                    for i in range(self.att):
                        if integer[i]==False:
                            init_pos.append(random.uniform(l_bound[i],u_bound[i]))
                        else:
                            init_pos.append(random.randint(l_bound[i],u_bound[i]))
                    self.position = np.array(init_pos)
                else:
                    if integer==False:
                        self.position= random.uniform(l_bound,u_bound)
                    else:
                        self.position= random.randint(l_bound,u_bound)
            except:
                print('We need lower and upper bound for init position')
        
        self.obj_values =self.calc_obj_value()
        
        if np.all(np.isnan(velocity))==False:
            self.velocity = velocity
        else:
            try:
                if attribute_number!=1:
                    self.velocity = np.array([random.uniform(-vmax[i],vmax[i]) for i in range(self.att)])
                else:
                    self.velocity = random.uniform(-vmax,vmax)
            except:
                print('we need an vmax for init velocity')
        self.best_p=np.nan
        self.S = []
        self.n = np.nan
        self.rank = np.nan
        self.distance = np.nan
        
    def __repr__(self):
        return f"Single objective particle with: \n\t position {self.position} \n \t velocity {self.velocity} \n\t objective value {self.obj_values} \n\t rank {self.rank} \n\t and crowding distance {self.distance}"
        
    def set_position(self,new_pos):
        self.position = new_pos
        self.obj_values = self.calc_obj_value()
    
    def get_obj_value(self):
        return self.obj_values
    
    def init_p_best(self):
        self.best_p = particle_multi(self.obj_functions,self.att,constr=self.constraints,position=self.position,velocity=self.velocity)
        self.best_p.rank  = self.rank
        self.best_p.distance = self.distance
        
    def compare_p_best(self):
        if self.compare_rank_dist(self.rank,self.distance,self.best_p.rank,self.best_p.distance):
            self.best_p.set_position(self.position)
            self.best_p.rank = self.rank
            self.best_p.distance = self.distance
        
    def compare(self,part2):
        return self.compare_rank_dist(self.rank,self.distance,part2.rank,part2.distance)

        
    def plot(self,best_p,x_coord,y_coord):
        if best_p:
            if self.best_p.rank==0:
                plt.plot(self.best_p.obj_values[x_coord],self.best_p.obj_values[y_coord],'r*')
            else:
                plt.plot(self.best_p.obj_values[x_coord],self.best_p.obj_values[y_coord],'k.')
        else:
            if self.rank == 0:
                plt.plot(self.obj_values[x_coord],self.obj_values[y_coord],'r*')
            else:
                plt.plot(self.obj_values[x_coord],self.obj_values[y_coord],'k.')

        
    def compare_rank_dist(self,rank_1,distance_1,rank_2,distance_2):
        if rank_1 == rank_2:
            if distance_1 == distance_2:
                return random.randint(0,1)
            else: 
                return distance_1>distance_2
        else:
            return rank_1<rank_2
    
    def dominates(self,part2):
        dom=True
        for i in range(len(self.obj_values)):
            less = self.obj_values[i]<=part2.obj_values[i]
            dom*=less
        return dom
    
    def calc_obj_value(self):
        if not self.constraints:
            return np.array([func(self.position) for func in self.obj_functions])
        else:
            penalty = sum([con(self.position) for con in self.constraints])
            return np.array([func(self.position) for func in self.obj_functions]) + penalty
         
    
    

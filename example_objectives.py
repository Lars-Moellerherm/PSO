import numpy as np
def objective(prob):
    V = []
    l_bound = []
    u_bound = []
    f = []
    c = []

    #Problem 1: Binh and Korn
    
    def f1(x):
        return 4*x[0]**2 + 4*x[1]**2
    
    def f2(x):
        return (x[0]-5)**2+(x[1]-5)**2
    
    def g1(x):
        g = (x[0]-5)**2 + x[1]**2 - 25
        return g if g > 0 else 0

    def g2(x):
        g = (x[0]-8)**2 + (x[1]+3)**2 - 7.7
        return g if g < 0 else 0

    V.append(2)
    l_bound.append(np.array([0,0]))
    u_bound.append(np.array([5,3]))
    f.append([f1,f2])
    c.append([g1,g2])
    
    # Problem 2: Banana
    
    def banana(x):
        x1 = x[0]
        x2 = x[1]
        return x1**4 - 2*x2*x1**2 + x2**2 + x1**2 - 2*x1 + 5
    
    def con(x):
        x1 = x[0]
        x2 = x[1]
        return abs(-(x1 + 0.25)**2 + 0.75*x2)

    V.append(2)
    l_bound.append([-3, -1])
    u_bound.append([2, 6])
    f.append(banana)
    c.append(con)
    
    # Problem 3: Ackley function
    
    def ackley(x):
        return -20*np.exp(-0.2*np.sqrt(0.5*(x[0]**2+x[1]**2)))-np.exp(0.5*(np.cos(2*np.pi*x[0])+np.cos(2*np.pi*x[1])))+np.exp(1)+20
    
    V.append(2)
    l_bound.append([-5.12, -5.12])
    u_bound.append([5.12, 5.12])
    f.append(ackley)
    c.append([])
    
    return V[prob-1], l_bound[prob-1], u_bound[prob-1], f[prob-1], c[prob-1]


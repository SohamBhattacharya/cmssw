import numpy

import ROOT


def CrystalBall(x, l_par) :
    
    alpha = l_par[0]
    n     = l_par[1]
    mu    = l_par[2]
    sigma = l_par[3]
    
    
    if (sigma < 0) :
        
        return 0
    
    
    z = (x - mu) / sigma

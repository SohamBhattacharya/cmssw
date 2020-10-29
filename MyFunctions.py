import numpy

import ROOT


#class Cruijiff :
#    
#    def __call__(self, x, parameters):
#        
#        x = x[0]
#        
#        mean   = parameters[0]
#        sigmaL = parameters[1]
#        sigmaR = parameters[2]
#        alphaL = parameters[3]
#        alphaR = parameters[4]
#        
#        dx = x - mean
#        
#        sigma = sigmaL
#        alpha = alphaL
#        
#        if (dx > 0) :
#            
#            sigma = sigmaR
#            alpha = alphaR
#        
#        f = 2*sigma*sigma + alpha*dx*dx
#        
#        if (not f) :
#            
#            return 0.0
#        
#        y = numpy.exp(-dx*dx/f)
#        
#        return y


def func_cruijiff(x, l_param) :
    
    x = x[0]
    
    norm   = l_param[0]
    mean   = l_param[1]
    sigmaL = l_param[2]
    sigmaR = l_param[3]
    alphaL = l_param[4]
    alphaR = l_param[5]
    
    dx = x - mean
    
    sigma = sigmaL
    alpha = alphaL
    
    if (dx > 0) :
        
        sigma = sigmaR
        alpha = alphaR
    
    f = 2*sigma*sigma + alpha*dx*dx
    
    if (not f) :
        
        return 0.0
    
    y = norm * numpy.exp(-dx*dx/f)
    
    return y


def get_cruijiff(xMin, xMax, name = "Cruijiff") :
    
    # No. of parameters = 5
    #f1 = ROOT.TF1(name, Cruijiff(), xMin, xMax, 5)
    f1 = ROOT.TF1(name, func_cruijiff, xMin, xMax, 6)
    
    f1.SetParName(0, "Norm")
    f1.SetParName(1, "Mean")
    f1.SetParName(2, "SigmaL")
    f1.SetParName(3, "SigmaR")
    f1.SetParName(4, "AlphaL")
    f1.SetParName(5, "AlphaR")
    
    return f1
    

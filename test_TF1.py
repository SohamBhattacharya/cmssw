import numpy
import time

import ROOT



class Cruijiff :
    
    def __call__(self, x, l_param):
        #(x, mean, sigmaL, sigmaR, alphaL, alphaR) :
        
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
        
        y = numpy.exp(-dx*dx/f)
        
        return y


# xMin, xMax, nPar
#f1 = ROOT.TF1("f1", Cruijiff(), 0, 2, 5)
#
#f1.SetParameter(0, 1.0)
#f1.SetParameter(1, 0.3)
#f1.SetParameter(2, 0.1)
#f1.SetParameter(3, 2)
#f1.SetParameter(4, 1)
#
#
#f1.Draw()


f1 = ROOT.TF1("f1", "cruijiff", 0.5, 1.5)

#f1.SetParameter(0, 1.0)
#f1.SetParameter(1, 0.3)
#f1.SetParameter(2, 0.1)
#f1.SetParameter(3, 2)
#f1.SetParameter(4, 1)

ROOT.c1.SetLogy(True)
ROOT.c1.Update()


time.sleep(100000)

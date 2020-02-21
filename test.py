import numpy


l1 = numpy.loadtxt("/home/soham/Desktop/test1.txt", dtype = "str", delimiter = "xxxxxxxxxxxxxxxxxxxxx")
l2 = numpy.loadtxt("/home/soham/Desktop/test2.txt", dtype = "str", delimiter = "xxxxxxxxxxxxxxxxxxxxx")

for iEle, ele in enumerate(l1) :
    
    idx1 = ele.find("> v")+2
    idx2 = ele.find(";")
    
    ele = ele[idx1: idx2]
    
    l1[iEle] = ele
    
    
    l_match = [ele in l2_ele for l2_ele in l2]
    
    if (not sum(l_match)) :
        
        print "Not found: %s" %(ele)

#print l1
print len(l1), len(l2)

#for ele

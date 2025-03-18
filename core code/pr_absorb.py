import numpy as np
import scipy.special as sp

class pr_absorb(object):
    def __init__(self,**kwargs):
        self.d = kwargs.get("d", 3)
        self.nu = (self.d-2)/2

    def __call__(self, cr2):
        return np.power(np.sqrt(cr2),self.nu)/(np.power(2,self.nu)*sp.gamma(self.nu+1)*sp.iv(self.nu,np.sqrt(cr2)))
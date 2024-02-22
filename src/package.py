"""
  The code belongs to Erwan Le Doeuff (weld).
  Feel free to contact me, erwan.le-doeuff AT etu.umontpellier.fr
"""

import numpy as np
import scipy.fft as fastft
from ctypes import CDLL, c_int
import matplotlib.pyplot as plt
from tifffile import imwrite, imread


class DDM:
    def  __init__(self, stack, Ndelays, mean_sampling_time):
        self.dim = stack.shape

        if Ndelays >= self.dim[0] :
            print("Ndelays should be stricly lesser than the number of images")

        self.Ndelays = Ndelays
        self.index_delays = np.arange(1,Ndelays+1).astype(np.int32)
        self.delays = self.index_delays * mean_sampling_time

        
        print("FFT transform ...")
        self.fft = fastft.fftn(stack, axes=(1,2), workers=-1).astype(np.complex128)
        
        # checker si la lib est là, sinon erreur
        libddm = CDLL("libddm.so")
        self.c_computeDDM = libddm.computeDDM

        self.c_computeDDM.restype = None
        self.c_computeDDM.argtypes = [c_int,
                                      c_int, c_int,
                                      np.ctypeslib.ndpointer(np.complex128, flags="C_CONTIGUOUS"), np.ctypeslib.ndpointer(np.double, flags="C_CONTIGUOUS"),
                                      c_int, np.ctypeslib.ndpointer(np.int32, flags="C_CONTIGUOUS")]
        

    def compute(self):
        ddm_dim = (self.Ndelays, self.dim[1], self.dim[-1])
        ddm = np.zeros(ddm_dim, dtype=np.double)
        print("Computing DDM ...")
        self.c_computeDDM(self.dim[0],
                          self.dim[-1], self.dim[1],
                          self.fft.ravel(), ddm.ravel(),
                          self.Ndelays, self.index_delays)
        
        return fastft.fftshift(ddm.reshape(ddm_dim), axes=(1,2))

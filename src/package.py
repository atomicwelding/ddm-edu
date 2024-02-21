import numpy as np
from ctypes import CDLL c_int
from tifffile import imwrite, imread

class DDM:
    def  __init__(self, stack, Ndelays, mean_sampling_time):
        self.dim = stack.shape

        if Ndelays >= self.dim[-1] :
            print("Ndelays should be stricly lesser than the number of images")

        self.Ndelays = Ndelays
        self.index_delays = np.arange(1,Ndelays+1).astype(np.int32)
        self.delays = self.index_delays * mean_sampling_time

        
        print("FFT transform ...")
        self.fft = np.fft.fftn(stack).astype(np.complex128).ravel()

        print(self.fft)

        # checker si la lib est là, sinon erreur
        libddm = CDLL("libddm.so")
        self.c_computeDDM = libddm.computeDDM

        self.c_computeDDM.restype = None
        self.c_computeDDM.argtypes = [c_int,
                                      c_int, c_int,
                                      np.ctypeslib.ndpointer(np.complex128, flags="C_CONTIGUOUS"), np.ctypeslib.ndpointer(np.double, flags="C_CONTIGUOUS"),
                                      c_int, np.ctypeslib.ndpointer(np.int32, flags="C_CONTIGUOUS")]
        

    def compute(self):
        ddm = np.zeros((self.dim[1], self.dim[0], self.Ndelays), dtype=np.double).ravel()
        print("Computing DDM ...")
        self.c_computeDDM(self.dim[-1],
                          self.dim[1], self.dim[0],
                          self.fft, ddm,
                          self.Ndelays, self.index_delays)
        return ddm.reshape((self.Ndelays,self.dim[1],self.dim[0]))

# example

# load image
image = imread('test.tif')
t,y,x = image.shape


# compute ddm
stack = image.reshape((y,x,t)).astype(np.double)
ddmstack = DDM(stack, 40, 0.07).compute()

# write file
imwrite("output.tif", ddmstack)

# ddm-edu

DDM python package for educational purposes. Refer to simd-ddm for efficient DDM software.

# install

Install the necessary tools to compile some c. Install `libomp`. 
Pull the repo and execute the following commands:

```sh
cd src
make
```

Beware that you may need to modify the `Makefile` in order to build `libddm`, as it depends on your platform. Feel free to contact me if needed.


# usage

```py
from ddm import DDM
import numpy as np
from tifffile import imwrite, imread
# load image
image = imread('sample.tif')

# compute ddm
stack = image.astype(np.double)
ddmstack = DDM(stack = stack, Ndelays = 300,  mean_sampling_time = 0.07) 
result = ddmstack.compute()

# write file
imwrite("output.tif", result)
```

To see a better example, check out the jupyter notebook.



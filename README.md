# ddm-edu

DDM python package for educational purposes. Refer to simd-ddm for efficient DDM software.

# usage

```py
import numpy as np
from tifffile import imwrite, imread
# load image
image = imread('sample.tif')

# compute ddm
stack = image.astype(np.double)
ddmstack = DDM(stack, 300, 0.07)
result = ddmstack.compute()

# write file
imwrite("output.tif", result)
```

To see a better example, check out the jupyter notebook.


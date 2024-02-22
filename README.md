# ddm-edu
DDM Python package for educational purpose. See simd-ddm for efficient ddm software.

# usage

```py
# load image
image = imread('sample.tif')

# compute ddm
stack = image.astype(np.double)
ddmstack = DDM(stack, 300, 0.07)
result = ddmstack.compute()

# write file
imwrite("output.tif", result)
```


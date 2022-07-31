import numpy as np

image1 = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7}
lenaImage = {0:0, 1:0, 2:0, 3:1, 4:2, 5:4, 6:6, 7:7}

relationInterEqualizedHistogramAndSpecifHistogram = {}
for intensityEqualized in range(0, 8):
    minim = np.Infinity
    for intensitySpecif in range(0, 8):
        if lenaImage[intensitySpecif] != 0:
            diff = abs(image1[intensityEqualized] - lenaImage[intensitySpecif])
            if diff < minim:
                minim = diff
                relationInterEqualizedHistogramAndSpecifHistogram[intensityEqualized] = intensitySpecif
print(relationInterEqualizedHistogramAndSpecifHistogram)

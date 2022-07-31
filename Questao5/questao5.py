from PIL import Image
import sys
import numpy as np        
sys.path.append('D:/Programming/PDI/Trabalho1/Questao2')  
sys.path.append('D:/Programming/PDI/Trabalho1/Questao3')  

from questao2 import generateHistogram, generateNormalizedHistogram, generateAccumulatedHistogram, generateVisualGraphic
from questao3 import generateRelationInterOriginalValueEqualizedValue, equalizeImage

def specifyHistogram(inputOriginalToEqualizeRelation, specificOriginalToEqualizeRelation, maxIntensityValue):
    relationInterEqualizedHistogramAndSpecifHistogram = {}

    for intensityEqualized in range(0, maxIntensityValue + 1):
        minDiff = np.Infinity

        for intensitySpecif in range(0, maxIntensityValue + 1):
            if specificOriginalToEqualizeRelation[intensitySpecif] != 0:
                diff = abs(inputOriginalToEqualizeRelation[intensityEqualized] - specificOriginalToEqualizeRelation[intensitySpecif])
                if diff < minDiff:
                    minDiff = diff
                    relationInterEqualizedHistogramAndSpecifHistogram[inputOriginalToEqualizeRelation[intensityEqualized]] = intensitySpecif

    return relationInterEqualizedHistogramAndSpecifHistogram

def intensityTransformationSpecify(image, relationInterEqualizedHistogramAndSpecifHistogram):
    lines = image.size[0]
    columns = image.size[1]

    for i in range(lines):
        for j in range(columns):
            intensity = image.getpixel((i, j))
            image.putpixel((i, j), relationInterEqualizedHistogramAndSpecifHistogram[intensity])

image1 = Image.open('Trabalho1\\image1.png')

lenaGrayImage = Image.open('Trabalho1\\lena_gray.bmp')

maxIntensityValue = 255

image1RelationInputToEqualize = generateRelationInterOriginalValueEqualizedValue(image1, maxIntensityValue)
lenaGrayRelationInputToEqualize = generateRelationInterOriginalValueEqualizedValue(lenaGrayImage, maxIntensityValue)

relationInterEqualizedHistogramAndSpecifHistogram = specifyHistogram(image1RelationInputToEqualize, lenaGrayRelationInputToEqualize, maxIntensityValue)

equalizeImage(image1, image1RelationInputToEqualize)

intensityTransformationSpecify(image1, relationInterEqualizedHistogramAndSpecifHistogram)
        
specifyImageHistogram = generateHistogram(image1, maxIntensityValue)
generateVisualGraphic(specifyImageHistogram, "red", 'Intensidade', 'Quantidade de pixels', 'Histograma especificado', 'Trabalho1\Questao5\\specifyHistogram.png')

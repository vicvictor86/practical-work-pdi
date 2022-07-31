from PIL import Image
import sys        
sys.path.append('D:/Programming/PDI/Trabalho1/Questao2')  
from questao2 import generateHistogram, generateNormalizedHistogram, generateAccumulatedHistogram, generateVisualGraphic

def generateRelationInterOriginalValueEqualizedValue(image, maxIntensityValue):
    histogram = generateHistogram(image, maxIntensityValue)
    normalizedHistogram = generateNormalizedHistogram(histogram, maxIntensityValue, image)
    accumulatedHistogram = generateAccumulatedHistogram(normalizedHistogram, maxIntensityValue)

    originalValueToNormalizedValue = {}
    for originalValue in histogram:
        stepOneEqualization = maxIntensityValue * accumulatedHistogram[originalValue]
        normalizedValue = round(stepOneEqualization)
        originalValueToNormalizedValue[originalValue] = normalizedValue

    return originalValueToNormalizedValue

def equalizeImage(image, relationOriginalToEqualized):
    lines = image.size[0]
    columns = image.size[1]

    for i in range(lines):
        for j in range(columns):
            image.putpixel((i,j), relationOriginalToEqualized[image.getpixel((i, j))])

def differenceBetweenImages(image1, image2):
    lines = image1.size[0]
    columns = image1.size[1]

    diffImage = Image.new(image1.mode, image1.size)
    for i in range(lines):
        for j in range(columns):
            diffImage.putpixel((i,j), image1.getpixel((i, j)) - image2.getpixel((i, j)))
    return diffImage

if __name__ == '__main__':
    image1 = Image.open('Trabalho1\\image1.png')

    lenaGrayImage = Image.open('Trabalho1\\lena_gray.bmp')

    maxIntensityValue = 255

    image1RelationOriginalToEqualized = generateRelationInterOriginalValueEqualizedValue(image1, maxIntensityValue)
    lenaGrayRelationOriginalToEqualized = generateRelationInterOriginalValueEqualizedValue(lenaGrayImage, maxIntensityValue)

    originalHistogramImage1 = generateHistogram(image1, maxIntensityValue)
    originalHistogramLena = generateHistogram(lenaGrayImage, maxIntensityValue)
    generateVisualGraphic(originalHistogramImage1, 'blue', 'Intensidade', 'Quantidade de pixels', 'Histograma da imagem 1', 'D:\Programming\PDI\Trabalho1\Questao3\Image1Histograms\image1.png')
    generateVisualGraphic(originalHistogramLena, 'blue', 'Intensidade', 'Quantidade de pixels', 'Histograma da Lena', 'D:\Programming\PDI\Trabalho1\Questao3\LenaHistograms\lena.png')

    image1.save("D:\Programming\PDI\Trabalho1\Questao3\Image1Results\image1_not_equalized.png")
    lenaGrayImage.save("D:\Programming\PDI\Trabalho1\Questao3\LenaResults\lena_gray_not_equalized.bmp")

    equalizeImage(image1, image1RelationOriginalToEqualized)
    equalizeImage(lenaGrayImage, lenaGrayRelationOriginalToEqualized)

    equalizedHistogramImage1 = generateHistogram(image1, maxIntensityValue)
    equalizedHistogramLena = generateHistogram(lenaGrayImage, maxIntensityValue)
    generateVisualGraphic(equalizedHistogramImage1, 'blue', 'Intensidade', 'Quantidade de pixels', 'Histograma equalizado da imagem 1', 'D:\Programming\PDI\Trabalho1\Questao3\Image1Histograms\image1_equalized.png')
    generateVisualGraphic(equalizedHistogramLena, 'blue', 'Intensidade', 'Quantidade de pixels', 'Histograma equalizado da Lena', 'D:\Programming\PDI\Trabalho1\Questao3\LenaHistograms\lena_equalized.png')

    image1.save("D:\Programming\PDI\Trabalho1\Questao3\Image1Results\image1_equalized.png")
    lenaGrayImage.save("D:\Programming\PDI\Trabalho1\Questao3\LenaResults\lena_gray_equalized.bmp")

    image1RelationOriginalToEqualizedTwoTimes = generateRelationInterOriginalValueEqualizedValue(image1, maxIntensityValue)
    equalizeImage(image1, image1RelationOriginalToEqualizedTwoTimes)
    image1.save("D:\Programming\PDI\Trabalho1\Questao3\Image1Results\image1_equalized_two_times.png")

    lenaRelationOriginalToEqualizedTwoTimes = generateRelationInterOriginalValueEqualizedValue(lenaGrayImage, maxIntensityValue)
    equalizeImage(lenaGrayImage, lenaRelationOriginalToEqualizedTwoTimes)
    lenaGrayImage.save("D:\Programming\PDI\Trabalho1\Questao3\LenaResults\lena_gray_equalized_two_times.bmp")

    image1FirstEqualized = Image.open("D:\Programming\PDI\Trabalho1\Questao3\Image1Results\image1_equalized.png")
    diffImage1 = differenceBetweenImages(image1, image1FirstEqualized)
    diffImage1.save("D:\Programming\PDI\Trabalho1\Questao3\Diffs\diff_image1.bmp")

    lenaImageFirstEqualized = Image.open("D:\Programming\PDI\Trabalho1\Questao3\LenaResults\lena_gray_equalized.bmp")
    diffImageLena = differenceBetweenImages(lenaGrayImage, lenaImageFirstEqualized)
    diffImageLena.save("D:\Programming\PDI\Trabalho1\Questao3\Diffs\diff_image_lena.bmp")

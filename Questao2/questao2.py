from PIL import Image
import matplotlib.pyplot as plt

def generateVisualGraphic(histogram, color, xLabel, yLabel, title, path):
    xValues = list(histogram.keys())
    yValues = list(histogram.values())
    plt.hist(xValues, bins=256, weights=yValues, color=color)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.savefig(path)
    plt.close()

def generateHistogram(image, maxIntensityValue):
    lines = image.size[0]
    columns = image.size[1]
    pixels = image.load()
    
    histogram = {}
    for i in range(0, maxIntensityValue + 1):
        histogram[i] = 0

    for i in range(lines):
        for j in range(columns):
            histogram[pixels[i, j]] = histogram.get(pixels[i, j], 0) + 1

    return histogram

def generateNormalizedHistogram(histogram, maxIntensityValue, image):
    lines = image.size[0]
    columns = image.size[1]

    normalizedHistogram = {}

    quantityOfPixels = (columns*lines)
    for i in range(0, maxIntensityValue + 1):
        normalizedHistogram[i] = histogram.get(i, 0) / quantityOfPixels

    return normalizedHistogram

def generateAccumulatedHistogram(normalizedHistogram, maxIntensityValue):
    accumulatedHistogram = {}

    for i in range(0, maxIntensityValue + 1):
        accumulatedHistogram[i] = accumulatedHistogram.get(i - 1, 0) + normalizedHistogram[i]

    return accumulatedHistogram

if __name__ == '__main__':
    image = Image.open('Trabalho1\\lena_gray.bmp')
    maxIntensityValue = 255

    histogram = generateHistogram(image, maxIntensityValue)
    normalizedHistogram = generateNormalizedHistogram(histogram, maxIntensityValue, image)
    accumulatedHistogram = generateAccumulatedHistogram(normalizedHistogram, maxIntensityValue)

    generateVisualGraphic(histogram, 'red', 'Valores de intensidade', 'Quantidade de pixels', 'Histograma', 'Trabalho1\Questao2\Figs\histogram.png')
    generateVisualGraphic(normalizedHistogram, 'red', 'Valores de intensidade', 'Proporções dos pixels', 'Histograma normalizado', 'Trabalho1\Questao2\Figs\\normalizedHistogram.png')
    generateVisualGraphic(accumulatedHistogram, 'red', 'Valores de intensidade', 'Proporções dos pixels', 'Histograma acumulado', 'Trabalho1\Questao2\Figs\\accumulatedHistogram.png')

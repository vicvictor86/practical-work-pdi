from PIL import Image
import math

def transformationA(image, b, c):
    newImage = Image.new(image.mode, image.size)
    lines = image.size[0]
    columns = image.size[1]

    for i in range(lines):
        for j in range(columns):
            newImage.putpixel((i,j), round(c * image.getpixel((i, j)) + b))
    return newImage

def transformationB(image, c):
    newImage = Image.new(image.mode, image.size)
    lines = image.size[0]
    columns = image.size[1]
    
    for i in range(lines):
        for j in range(columns):
            logResult = math.log2(image.getpixel((i, j)) + 1)
            finalResult = round(c * logResult)
            newImage.putpixel((i,j), finalResult)
    return newImage

def transformationC(image, c, gama):
    newImage = Image.new(image.mode, image.size)
    lines = image.size[0]
    columns = image.size[1]
    
    for i in range(lines):
        for j in range(columns):
            finalResult = round(c * math.pow(image.getpixel((i, j)) + 1, gama))
            newImage.putpixel((i,j), finalResult)
    
    return newImage

imageA = Image.open('Trabalho1\\lena_gray.bmp')
pixelsA = imageA.load()

imageB = Image.open('Trabalho1\\lena_gray.bmp')
pixelsB = imageB.load()

imageC = Image.open('Trabalho1\\lena_gray.bmp')
pixelsC = imageC.load()

maxIntensityValue = 255

cForLog = 255 / math.log2(1 + maxIntensityValue)
constantsA = {"b": [0, 60, 120], "c": [1, 2]}
constantsB = {"c": [1, 20, cForLog]}
constantsC = {"c": [2, 5], "gama": [0.4, 0.7, 1.2]}

firstImageA = transformationA(imageA, constantsA["b"][0], constantsA["c"][1])
firstImageA.save('Trabalho1\\questao4\\transformationA\\firstImage.bmp')

secondImageA = transformationA(imageA, constantsA["b"][1], constantsA["c"][0])
secondImageA.save('Trabalho1\\questao4\\transformationA\\secondImage.bmp')

thirdImageA = transformationA(imageA, constantsA["b"][2], constantsA["c"][0])
thirdImageA.save('Trabalho1\\questao4\\transformationA\\thirdImage.bmp')

firstImageB = transformationB(imageB, constantsB["c"][0])
firstImageB.save('Trabalho1\\questao4\\transformationB\\firstImage.bmp')

secondImageB = transformationB(imageB, constantsB["c"][1])
secondImageB.save('Trabalho1\\questao4\\transformationB\\secondImage.bmp')

thirdImageB = transformationB(imageB, cForLog)
thirdImageB.save('Trabalho1\\questao4\\transformationB\\thirdImage.bmp')

firstImageC = transformationC(imageC, constantsC["c"][1], constantsC["gama"][0])
firstImageC.save('Trabalho1\\questao4\\transformationC\\firstImage.bmp')

secondImageC = transformationC(imageC, constantsC["c"][0], constantsC["gama"][1])
secondImageC.save('Trabalho1\\questao4\\transformationC\\secondImage.bmp')

thirdImageC = transformationC(imageC, constantsC["c"][0], constantsC["gama"][2])
thirdImageC.save('Trabalho1\\questao4\\transformationC\\thirdImage.bmp')
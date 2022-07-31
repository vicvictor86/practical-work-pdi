from PIL import Image

def getNeighbors4(pixels, xPixel, yPixel):
    neighbors4 = []
    neighbors4.append(pixels[xPixel - 1, yPixel])
    neighbors4.append(pixels[xPixel + 1, yPixel])
    neighbors4.append(pixels[xPixel, yPixel - 1])
    neighbors4.append(pixels[xPixel, yPixel + 1])
    return neighbors4

def getNeighbors8(pixels, xPixel, yPixel):
    neighbors8 = getNeighbors4(pixels, xPixel, yPixel)
    neighbors8.append(pixels[xPixel - 1, yPixel - 1])
    neighbors8.append(pixels[xPixel + 1, yPixel - 1])
    neighbors8.append(pixels[xPixel - 1, yPixel + 1])
    neighbors8.append(pixels[xPixel + 1, yPixel + 1])
    return neighbors8

def checkAdjacency4(pixels, xPixel1, yPixel1, xPixel2, yPixel2, neighbors4=None):
    if neighbors4 is None:
        neighbors4 = getNeighbors4(pixels, xPixel1, yPixel1)

    pixelQ = pixels[xPixel2, yPixel2]
    if pixelQ in neighbors4 and pixelQ in setV:
        return True
    else:
        return False
    
def checkAdjacency8(pixels, xPixel1, yPixel1, xPixel2, yPixel2, neighbors8=None):
    if neighbors8 is None:
        neighbors8 = getNeighbors8(pixels, xPixel1, yPixel1)

    pixelQ = pixels[xPixel2, yPixel2]
    try:
        if pixelQ in neighbors8 and pixelQ in setV:
            return True
        else:
            return False
    except IndexError:
        return True

def checkAllAdjacencies4(pixels, xPixel1, yPixel1):
    neighbors4 = getNeighbors4(pixels, xPixel1, yPixel1)

    adjacencyWithLeftPixel = checkAdjacency4(pixels, xPixel1, yPixel1, xPixel1 - 1, yPixel1, neighbors4)
    adjacencyWithRightPixel = checkAdjacency4(pixels, xPixel1, yPixel1, xPixel1 + 1, yPixel1, neighbors4)
    adjacencyWithuUpixel = checkAdjacency4(pixels, xPixel1, yPixel1, xPixel1, yPixel1 - 1, neighbors4)
    adjacencyWithDownPixel = checkAdjacency4(pixels, xPixel1, yPixel1, xPixel1, yPixel1 + 1, neighbors4)
    if(adjacencyWithLeftPixel and adjacencyWithRightPixel and adjacencyWithuUpixel and adjacencyWithDownPixel):
        return True
    else:
        return False

def checkAllAdjacencies8(pixels, xPixel1, yPixel1):
    neighbors8 = getNeighbors8(pixels, xPixel1, yPixel1)

    adjacencyWithLeftPixel = checkAdjacency8(pixels, xPixel1, yPixel1, xPixel1 - 1, yPixel1, neighbors8)
    adjacencyWithRightPixel = checkAdjacency8(pixels, xPixel1, yPixel1, xPixel1 + 1, yPixel1, neighbors8)
    adjacencyWithuUpixel = checkAdjacency8(pixels, xPixel1, yPixel1, xPixel1, yPixel1 - 1, neighbors8)
    adjacencyWithDownPixel = checkAdjacency8(pixels, xPixel1, yPixel1, xPixel1, yPixel1 + 1, neighbors8)

    adjacencyWithLeftUpPixel = checkAdjacency8(pixels, xPixel1, yPixel1, xPixel1 - 1, yPixel1 - 1, neighbors8)
    adjacencyWithRightUpPixel = checkAdjacency8(pixels, xPixel1, yPixel1, xPixel1 + 1, yPixel1 - 1, neighbors8)
    adjacencyWithLeftDownPixel = checkAdjacency8(pixels, xPixel1, yPixel1, xPixel1 - 1, yPixel1 + 1, neighbors8)
    adjacencyWithRightDownPixel = checkAdjacency8(pixels, xPixel1, yPixel1, xPixel1 + 1, yPixel1 + 1, neighbors8)

    adjacencyNeighbor4 = adjacencyWithLeftPixel and adjacencyWithRightPixel and adjacencyWithuUpixel and adjacencyWithDownPixel
    adjacencyNeighborDiagonal = adjacencyWithLeftUpPixel and adjacencyWithRightUpPixel and adjacencyWithLeftDownPixel and adjacencyWithRightDownPixel
    if(adjacencyNeighbor4 and adjacencyNeighborDiagonal):
        return True
    else:
        return False

def paintBorder(pixels, listOfBordersAdjacency):
    for border in listOfBordersAdjacency:
        pixels[border['x'], border['y']] = (255, 0, 0, 255)

def changeObjectColor(image, pixels):
    lines = image.size[0]
    columns = image.size[1]
    white = (255, 255, 255, 255)
    black = (0, 0, 0, 255)

    for i in range(lines):
        for j in range(columns):
            if pixels[i, j] == white:
                pixels[i, j] = black

def showAndSaveImage(image, path):
    image.save(path)
    image.show()

def addToListOfBordersAdjacency(image, pixels, checkAllAdjacenciesType):
    listOfBordersAdjacency = []
    lines = image.size[0]
    columns = image.size[1]
    
    for i in range(lines):
        for j in range(columns):
            pixelP = pixels[i, j]
            if(pixelP in setV and not checkAllAdjacenciesType(pixels, i, j)):
                listOfBordersAdjacency.append({'x': i, 'y': j})
    return listOfBordersAdjacency

imageAdjacency4 = Image.open('Trabalho1\\folha.png')
pixelsAdjacency4 = imageAdjacency4.load()

imageAdjacency8 = Image.open('Trabalho1\\folha.png')
pixelsAdjacency8 = imageAdjacency8.load()

setV = [(255, 255, 255, 255)]

listOfBordersAdjacency4 = addToListOfBordersAdjacency(imageAdjacency4, pixelsAdjacency4, checkAllAdjacencies4)

listOfBordersAdjacency8 = addToListOfBordersAdjacency(imageAdjacency8, pixelsAdjacency8, checkAllAdjacencies8)

paintBorder(pixelsAdjacency4, listOfBordersAdjacency4)
changeObjectColor(imageAdjacency4, pixelsAdjacency4)

paintBorder(pixelsAdjacency8, listOfBordersAdjacency8)
changeObjectColor(imageAdjacency8, pixelsAdjacency8)

showAndSaveImage(imageAdjacency4, 'Trabalho1\\folha_adjacency4.png')
showAndSaveImage(imageAdjacency8, 'Trabalho1\\folha_adjacency8.png')

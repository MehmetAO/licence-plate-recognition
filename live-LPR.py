import cv2
import imutils
import numpy as np
import pytesseract
from picamera.array import PiRGBArray
from picamera import PiCamera

# Tesseract location for windows
# For linux just remove the line
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def importImage(img_location): # Importing image
    img = cv2.imread(img_location, cv2.IMREAD_COLOR)
    #img = cv2.resize(img, (600, 400))

    return img

def grayScale(img): # Turning image to black and white to process
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 13, 15, 15)

    return gray

def edgingImage(img): #Edges
    edged = cv2.Canny(img, 30, 200)

    return edged

def contouringImage(edged_image): # Contouring the image so we can find a rectangle which will our licence plate
    contours = cv2.findContours(edged_image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
    screenCnt = None

    return contours

def findingPlate(contours, img_location): # Finding rectangle and return it as a tuple
    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)

        if len(approx) == 4:
            screenCnt = approx
            break

    if screenCnt is None:
        detected = 0
        print("No contour detected")
    else:
        detected = 1

    if detected == 1:
        cv2.drawContours(importImage(img_location), [screenCnt], -1, (0, 0, 255), 3)

    return screenCnt

def localisation(licensePlateRAW): # Removing errors which can be occur because of Turkish license plates stamps
    licensePlate = []
    for i in licensePlateRAW:
        if i.isalpha() and i.isupper():
            licensePlate.append(i)
        elif i.isnumeric():
            licensePlate.append(i)
    return licensePlate

def main(image_location):
    #Setup cam
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 30

    rawCapture = PiRGBArray(camera, size=(640, 480))

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        grayScaledImage = grayScale(image)  # Turning our image gray
        edged = edgingImage(grayScaledImage)  # Emphasize edges
        contour = contouringImage(edged)  # Contouring the edges
        licensePlate = findingPlate(contour, image_location)  # License plates location

        # Masking the useless part
        mask = np.zeros(grayScaledImage.shape, np.uint8)
        new_image = cv2.drawContours(mask, [licensePlate], 0, 255, -1, )
        new_image = cv2.bitwise_and(image, image, mask=mask)

        # Croping masked area
        (x, y) = np.where(mask == 255)
        (topx, topy) = (np.min(x), np.min(y))
        (bottomx, bottomy) = (np.max(x), np.max(y))
        Cropped = grayScaledImage[topx:bottomx + 1, topy:bottomy + 1]

        # Read the number plate from cropted image
        plateNumber = pytesseract.image_to_string(Cropped, config='--psm 11')

        # List version of final data
        listLP = localisation(plateNumber)
        print("Araç plakası:", listLP)

        return listLP

if __name__ == "__main__":
    main("test.jpg")
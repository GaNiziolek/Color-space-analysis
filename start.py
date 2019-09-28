import cv2
import numpy as np
import imutils
import os

from trackbars import txTrackbars as tX_tB

tB = tX_tB()

path = 'imagem-teste\placas-vermelhas.jpg'

print(path)

if not os.path.exists(path):
    print('Caminho ou Imagem não existem!')
    exit()

image_src = cv2.imread(path)

if image_src is None:
    print('ERROR: Img is None')
    cv2.destroyAllWindows()
    exit()

while True:
    k = cv2.waitKey(1)
    if k == 27:  # Tecla 'esc'
        break

    blurvalue = cv2.getTrackbarPos('Blur', tB.tran)
    print(blurvalue)
    image_blur = cv2.blur(image_src.copy(), (blurvalue+1, blurvalue+1))
    erode = cv2.getTrackbarPos('Erode', tB.tran)
    dilate = cv2.getTrackbarPos('Dilate', tB.tran)

    eroded = cv2.erode(image_blur, None, iterations=(erode+1))
    dilated = cv2.dilate(eroded, None, iterations=(dilate+1))

    image_bgr = dilated.copy()
    image_hsv = cv2.cvtColor(dilated, cv2.COLOR_BGR2HSV)
    image_lab = cv2.cvtColor(dilated, cv2.COLOR_BGR2LAB)
    image_YCrCb = cv2.cvtColor(dilated, cv2.COLOR_BGR2YCrCb)

    tB_Read = tB.readTrackbars()

    # make array for final values
    lower_hsv = np.array([tB_Read.hul, tB_Read.sal, tB_Read.val])  # TODO AttributeError: 'NoneType' object has no attribute 'hul'
    upper_hsv = np.array([tB_Read.huh, tB_Read.sah, tB_Read.vah])

    lower_bgr = np.array([tB_Read.bluel, tB_Read.greenl, tB_Read.redl])
    upper_bgr = np.array([tB_Read.blueh, tB_Read.greenh, tB_Read.redh])

    lower_lab = np.array([tB_Read.lightl, tB_Read.g_rl, tB_Read.b_yl])
    upper_lab = np.array([tB_Read.lighth, tB_Read.g_rh, tB_Read.b_yh])

    lower_YCrCb = np.array([tB_Read.lumal, tB_Read.Ycrl, tB_Read.YCbl])
    upper_YCrCb = np.array([tB_Read.lumah, tB_Read.Ycrh, tB_Read.Ycbh])

    # create a mask for that range
    mask_hsv = cv2.inRange(image_hsv, lower_hsv, upper_hsv)
    res_hsv = cv2.bitwise_and(image_hsv, image_hsv, mask=mask_hsv)

    mask_bgr = cv2.inRange(image_bgr, lower_bgr, upper_bgr)
    res_bgr = cv2.bitwise_and(image_bgr, image_bgr, mask=mask_bgr)

    mask_lab = cv2.inRange(image_lab, lower_lab, upper_lab)
    res_lab = cv2.bitwise_and(image_lab, image_lab, mask=mask_lab)

    mask_YCrCb = cv2.inRange(image_YCrCb, lower_YCrCb, upper_YCrCb)
    res_YCrCb = cv2.bitwise_and(image_YCrCb, image_YCrCb, mask=mask_YCrCb)

    cv2.imshow('HSV', res_hsv)
    cv2.imshow('BGR', res_bgr)
    cv2.imshow('LAB', res_lab)
    cv2.imshow('YCrCb', res_YCrCb)

    # CALLBACK FUNCTION
    cv2.setMouseCallback("HSV", tX_tB.pick_color_hsv(image=image_hsv))
    cv2.setMouseCallback("BGR", tX_tB.pick_color_bgr(image=image_bgr))
    cv2.setMouseCallback("LAB", tX_tB.pick_color_lab(image=image_lab))
    cv2.setMouseCallback("YCrCb", tX_tB.pick_color_YCrCb(image=image_YCrCb))

print('HSV:')
print(lower_hsv)
print(upper_hsv)
print('BGR:')
print(lower_bgr)
print(upper_bgr)
print('LAB:')
print(lower_lab)
print(upper_lab)
print('YCrCb:')
print(lower_YCrCb)
print(upper_YCrCb)

cv2.destroyAllWindows()

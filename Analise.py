import cv2
import numpy as np
import imutils
import os

def nothing(x):
    pass  

def pick_color_bgr(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = image_bgr[y,x]

        #HUE, SATURATION, AND VALUE (BRIGHTNESS) RANGES. TOLERANCE COULD BE ADJUSTED.
        cv2.setTrackbarPos(bl, bgrt, pixel[0] - bluer)
        cv2.setTrackbarPos(bh, bgrt, pixel[0] + bluer)
        cv2.setTrackbarPos(gl, bgrt, pixel[1] - greenr)
        cv2.setTrackbarPos(gh, bgrt, pixel[1] + greenr)
        cv2.setTrackbarPos(rl, bgrt, pixel[2] - redr)
        cv2.setTrackbarPos(rh, bgrt, pixel[2] + redr)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.setTrackbarPos(bl, bgrt, 0)
        cv2.setTrackbarPos(bh, bgrt, 255)
        cv2.setTrackbarPos(gl, bgrt, 0)
        cv2.setTrackbarPos(gh, bgrt, 255)
        cv2.setTrackbarPos(rl, bgrt, 0)
        cv2.setTrackbarPos(rh, bgrt, 255)

def pick_color_hsv(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = image_hsv[y,x]

        #HUE, SATURATION, AND VALUE (BRIGHTNESS) RANGES. TOLERANCE COULD BE ADJUSTED.
        cv2.setTrackbarPos(hl, hsvt, pixel[0] - hur)
        cv2.setTrackbarPos(hh, hsvt, pixel[0] + hur)
        cv2.setTrackbarPos(sl, hsvt, pixel[1] - sar)
        cv2.setTrackbarPos(sh, hsvt, pixel[1] + sar)
        cv2.setTrackbarPos(vl, hsvt, pixel[2] - var)
        cv2.setTrackbarPos(vh, hsvt, pixel[2] + var)
    
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.setTrackbarPos(hl, hsvt, 0)
        cv2.setTrackbarPos(hh, hsvt, 179)
        cv2.setTrackbarPos(sl, hsvt, 0)
        cv2.setTrackbarPos(sh, hsvt, 255)
        cv2.setTrackbarPos(vl, hsvt, 0)
        cv2.setTrackbarPos(vh, hsvt, 255)

def pick_color_lab(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = image_lab[y,x]

        #HUE, SATURATION, AND VALUE (BRIGHTNESS) RANGES. TOLERANCE COULD BE ADJUSTED.
        cv2.setTrackbarPos(ll, labt, pixel[0] - lightr)
        cv2.setTrackbarPos(lh, labt, pixel[0] + lightr)
        cv2.setTrackbarPos(al, labt, pixel[1] - g_rr)
        cv2.setTrackbarPos(ah, labt, pixel[1] + g_rr)
        cv2.setTrackbarPos(bl, labt, pixel[2] - b_yr)
        cv2.setTrackbarPos(bh, labt, pixel[2] + b_yr)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.setTrackbarPos(ll, labt, 0)
        cv2.setTrackbarPos(lh, labt, 255)
        cv2.setTrackbarPos(al, labt, 0)
        cv2.setTrackbarPos(ah, labt, 255)
        cv2.setTrackbarPos(bl, labt, 0)
        cv2.setTrackbarPos(bh, labt, 255)

def pick_color_YCrCb(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = image_YCrCb[y,x]

        #HUE, SATURATION, AND VALUE (BRIGHTNESS) RANGES. TOLERANCE COULD BE ADJUSTED.
        cv2.setTrackbarPos(Yl, YCrCbt, pixel[0] - lumar)
        cv2.setTrackbarPos(Yh, YCrCbt, pixel[0] + lumar)
        cv2.setTrackbarPos(Crl, YCrCbt, pixel[1] - Ycrr)
        cv2.setTrackbarPos(Crh, YCrCbt, pixel[1] + Ycrr)
        cv2.setTrackbarPos(Cbl, YCrCbt, pixel[2] - Ycbr)
        cv2.setTrackbarPos(Cbh, YCrCbt, pixel[2] + Ycbr)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.setTrackbarPos(Yl, YCrCbt, 0)
        cv2.setTrackbarPos(Yh, YCrCbt, 255)
        cv2.setTrackbarPos(Crl, YCrCbt, 0)
        cv2.setTrackbarPos(Crh, YCrCbt, 310)
        cv2.setTrackbarPos(Cbl, YCrCbt, 0)
        cv2.setTrackbarPos(Cbh, YCrCbt, 271)

#assign strings for ease of coding

bh = 'Blue High'
bl = 'Blue Low'
br = 'Blue Range'
gh = 'Green High'
gl = 'Green Low'
gr = 'Green Range'
rh = 'Red High'
rl = 'Red Low'
rr = 'Red Range'

hh='Hue High'
hl='Hue Low'
hr = 'Hur Range'
sh='Saturation High'
sl='Saturation Low'
sr = 'Saturation Range'
vh='Value High'
vl='Value Low'
vr = 'Value Range'

lh = 'Lightness High'
ll = 'Lightness Low'
lr = 'Lightness Range'
ah = 'Green-Red High'
al = 'Green-Red Low'
ar = 'Green-Red Range'
bh = 'Blue-Yellow High'
bl = 'Blue-Yellow Low'
byr = 'Blue-Yellow Range'

Yh = 'Luminance High'
Yl = 'Luminance Low'
Yr = 'Luminance Range'
Crh = 'R-Y High'
Crl = 'R-Y Low'
Crr = 'R-Y Range'
Cbh = 'B-Y High'
Cbl = 'B-Y Low'
Cbr = 'B-Y Range'

tran = 'Transform'
bgrt = 'BGR Trackbars'
hsvt = 'HSV Trackbars'
labt = 'LAB Trackbars'
YCrCbt = 'YCrCb Trackbars'

path = 'C:\\Users\\ganiz\\Pictures\\superficie_2.jpeg'

print (path)

if not os.path.exists(path):
    print('Caminho ou Imagem não existem!')
    exit()

image_src = cv2.imread(path)

if image_src is None:
    print('ERROR: Img is None')
    cv2.destroyAllWindows()
    exit()

cv2.namedWindow(tran,0)
cv2.namedWindow(bgrt,0)
cv2.namedWindow(hsvt,0)
cv2.namedWindow(labt,0)
cv2.namedWindow(YCrCbt,0)

#Begin Creating trackbars for each
cv2.createTrackbar('Blur', tran,0,10,nothing)
cv2.createTrackbar('Erode', tran,0,10,nothing)
cv2.createTrackbar('Dilate', tran,0,10,nothing)

cv2.createTrackbar(bl, bgrt,0,255,nothing)
cv2.createTrackbar(bh, bgrt,255,255,nothing)
cv2.createTrackbar(br, bgrt,20,50,nothing)
cv2.createTrackbar(gl, bgrt,0,255,nothing)
cv2.createTrackbar(gh, bgrt,255,255,nothing)
cv2.createTrackbar(gr, bgrt,20,50,nothing)
cv2.createTrackbar(rl, bgrt,0,255,nothing)
cv2.createTrackbar(rh, bgrt,255,255,nothing)
cv2.createTrackbar(rr, bgrt,20,50,nothing)

cv2.createTrackbar(hl, hsvt,0,179,nothing)
cv2.createTrackbar(hh, hsvt,179,179,nothing)
cv2.createTrackbar(hr, hsvt,20,50,nothing)
cv2.createTrackbar(sl, hsvt,0,255,nothing)
cv2.createTrackbar(sh, hsvt,255,255,nothing)
cv2.createTrackbar(sr, hsvt,20,50,nothing)
cv2.createTrackbar(vl, hsvt,0,255,nothing)
cv2.createTrackbar(vh, hsvt,255,255,nothing)
cv2.createTrackbar(vr, hsvt,20,50,nothing)

cv2.createTrackbar(ll, labt,0,255,nothing)
cv2.createTrackbar(lh, labt,255,255,nothing)
cv2.createTrackbar(lr, labt,20,50,nothing)
cv2.createTrackbar(al, labt,0,255,nothing)
cv2.createTrackbar(ah, labt,255,255,nothing)
cv2.createTrackbar(ar, labt,20,50,nothing)
cv2.createTrackbar(bl, labt,0,255,nothing)
cv2.createTrackbar(bh, labt,255,255,nothing)
cv2.createTrackbar(byr, labt,20,50,nothing)

cv2.createTrackbar(Yl, YCrCbt,0,255,nothing)
cv2.createTrackbar(Yh, YCrCbt,255,255,nothing)
cv2.createTrackbar(Yr, YCrCbt,20,50,nothing)
cv2.createTrackbar(Crl, YCrCbt,0,310,nothing)
cv2.createTrackbar(Crh, YCrCbt,310,310,nothing)
cv2.createTrackbar(Crr, YCrCbt,20,50,nothing)
cv2.createTrackbar(Cbl, YCrCbt,0,271,nothing)
cv2.createTrackbar(Cbh, YCrCbt,271,271,nothing)
cv2.createTrackbar(Cbr, YCrCbt,20,50,nothing)

while True:
    k = cv2.waitKey(1)
    if k == 27: #Tecla 'esc'
        break

    blurvalue =cv2.getTrackbarPos('Blur', tran)
    image_blur = cv2.blur(image_src.copy(), (blurvalue+1,blurvalue+1))
    erode=cv2.getTrackbarPos('Erode', tran)
    dilate=cv2.getTrackbarPos('Dilate', tran)

    eroded = cv2.erode(image_blur, None, iterations=(erode+1))
    dilated = cv2.dilate(eroded, None, iterations=(dilate+1))

    image_bgr = dilated.copy()
    image_hsv = cv2.cvtColor(dilated, cv2.COLOR_BGR2HSV)
    image_lab = cv2.cvtColor(dilated, cv2.COLOR_BGR2LAB)
    image_YCrCb = cv2.cvtColor(dilated, cv2.COLOR_BGR2YCrCb)

    #read trackbar positions for each trackbar

    bluel=cv2.getTrackbarPos(bl, bgrt)
    blueh=cv2.getTrackbarPos(bh, bgrt)
    bluer=cv2.getTrackbarPos(br, bgrt)
    greenl=cv2.getTrackbarPos(gl, bgrt)
    greenh=cv2.getTrackbarPos(gh, bgrt)
    greenr=cv2.getTrackbarPos(gr, bgrt)
    redl=cv2.getTrackbarPos(rl, bgrt)
    redh=cv2.getTrackbarPos(rh, bgrt)
    redr=cv2.getTrackbarPos(rr, bgrt)

    hul=cv2.getTrackbarPos(hl, hsvt)
    huh=cv2.getTrackbarPos(hh, hsvt)
    hur=cv2.getTrackbarPos(hr, hsvt)
    sal=cv2.getTrackbarPos(sl, hsvt)
    sah=cv2.getTrackbarPos(sh, hsvt)
    sar=cv2.getTrackbarPos(sr, hsvt)
    val=cv2.getTrackbarPos(vl, hsvt)
    vah=cv2.getTrackbarPos(vh, hsvt)
    var=cv2.getTrackbarPos(vr, hsvt)

    lightl=cv2.getTrackbarPos(ll, labt)
    lighth=cv2.getTrackbarPos(lh, labt)
    lightr=cv2.getTrackbarPos(lr, labt)
    g_rl=cv2.getTrackbarPos(al, labt)
    g_rh=cv2.getTrackbarPos(ah, labt) 
    g_rr=cv2.getTrackbarPos(ar, labt)                                                                   
    b_yl=cv2.getTrackbarPos(bl, labt)
    b_yh=cv2.getTrackbarPos(bh, labt)
    b_yr=cv2.getTrackbarPos(br, labt)

    lumal=cv2.getTrackbarPos(Yl, YCrCbt)
    lumah=cv2.getTrackbarPos(Yh, YCrCbt)
    lumar=cv2.getTrackbarPos(Yr, YCrCbt)
    Ycrl=cv2.getTrackbarPos(Crl, YCrCbt)
    Ycrh=cv2.getTrackbarPos(Crh, YCrCbt)
    Ycrr=cv2.getTrackbarPos(Crr, YCrCbt)
    YCbl=cv2.getTrackbarPos(Cbl, YCrCbt)
    Ycbh=cv2.getTrackbarPos(Cbh, YCrCbt)
    Ycbr=cv2.getTrackbarPos(Cbr, YCrCbt)

    #make array for final values
    lower_hsv = np.array([hul,sal,val])
    upper_hsv = np.array([huh,sah,vah])

    lower_bgr = np.array([bluel,greenl,redl])
    upper_bgr = np.array([blueh,greenh,redh])

    lower_lab = np.array([lightl,g_rl,b_yl])
    upper_lab = np.array([lighth,g_rh,b_yh])

    lower_YCrCb = np.array([lumal,Ycrl,YCbl])
    upper_YCrCb = np.array([lumah,Ycrh,Ycbh])

    #create a mask for that range
    mask_hsv = cv2.inRange(image_hsv,lower_hsv, upper_hsv)
    res_hsv = cv2.bitwise_and(image_hsv,image_hsv, mask =mask_hsv)

    mask_bgr = cv2.inRange(image_bgr,lower_bgr, upper_bgr)
    res_bgr = cv2.bitwise_and(image_bgr,image_bgr, mask =mask_bgr)

    mask_lab = cv2.inRange(image_lab,lower_lab, upper_lab)
    res_lab = cv2.bitwise_and(image_lab,image_lab, mask =mask_lab)

    mask_YCrCb = cv2.inRange(image_YCrCb,lower_YCrCb, upper_YCrCb)
    res_YCrCb = cv2.bitwise_and(image_YCrCb,image_YCrCb, mask =mask_YCrCb)

    cv2.imshow('HSV', res_hsv)
    cv2.imshow('BGR', res_bgr)
    cv2.imshow('LAB', res_lab)
    cv2.imshow('YCrCb', res_YCrCb)

    #CALLBACK FUNCTION
    cv2.setMouseCallback("HSV", pick_color_hsv)
    cv2.setMouseCallback("BGR", pick_color_bgr)
    cv2.setMouseCallback("LAB", pick_color_lab)
    cv2.setMouseCallback("YCrCb", pick_color_YCrCb)

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

import cv2


class Filters():
    
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

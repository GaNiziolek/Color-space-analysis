import cv2


class ignore():
    def nothing(self):
        pass


class txTrackbars():
    def __init__(self):

        # assign strings for ease of coding
        self.bh = 'Blue High'
        self.bl = 'Blue Low'
        self.br = 'Blue Range'
        self.gh = 'Green High'
        self.gl = 'Green Low'
        self.gr = 'Green Range'
        self.rh = 'Red High'
        self.rl = 'Red Low'
        self.rr = 'Red Range'

        self.hh = 'Hue High'
        self.hl = 'Hue Low'
        self.hr = 'Hur Range'
        self.sh = 'Saturation High'
        self.sl = 'Saturation Low'
        self.sr = 'Saturation Range'
        self.vh = 'Value High'
        self.vl = 'Value Low'
        self.vr = 'Value Range'

        self.lh = 'Lightness High'
        self.ll = 'Lightness Low'
        self.lr = 'Lightness Range'
        self.ah = 'Green-Red High'
        self.al = 'Green-Red Low'
        self.ar = 'Green-Red Range'
        self.bh = 'Blue-Yellow High'
        self.bl = 'Blue-Yellow Low'
        self.byr = 'Blue-Yellow Range'

        self.Yh = 'Luminance High'
        self.Yl = 'Luminance Low'
        self.Yr = 'Luminance Range'
        self.Crh = 'R-Y High'
        self.Crl = 'R-Y Low'
        self.Crr = 'R-Y Range'
        self.Cbh = 'B-Y High'
        self.Cbl = 'B-Y Low'
        self.Cbr = 'B-Y Range'

        self.tran = 'Transform'
        self.bgrt = 'BGR Trackbars'
        self.hsvt = 'HSV Trackbars'
        self.labt = 'LAB Trackbars'
        self.YCrCbt = 'YCrCb Trackbars'

        cv2.namedWindow(self.tran, 0)
        cv2.namedWindow(self.bgrt, 0)
        cv2.namedWindow(self.hsvt, 0)
        cv2.namedWindow(self.labt, 0)
        cv2.namedWindow(self.YCrCbt, 0)

        self.createTrackbars()

    def createTrackbars(self):
        cv2.createTrackbar('Blur', self.tran, 0, 10, ignore.nothing)
        cv2.createTrackbar('Erode', self.tran, 0, 10, ignore.nothing)
        cv2.createTrackbar('Dilate', self.tran, 0, 10, ignore.nothing)

        cv2.createTrackbar(self.bl, self.bgrt, 0, 255, ignore.nothing)
        cv2.createTrackbar(self.bh, self.bgrt, 255, 255, ignore.nothing)
        cv2.createTrackbar(self.br, self.bgrt, 20, 50, ignore.nothing)
        cv2.createTrackbar(self.gl, self.bgrt, 0, 255, ignore.nothing)
        cv2.createTrackbar(self.gh, self.bgrt, 255, 255, ignore.nothing)
        cv2.createTrackbar(self.gr, self.bgrt, 20, 50, ignore.nothing)
        cv2.createTrackbar(self.rl, self.bgrt, 0, 255, ignore.nothing)
        cv2.createTrackbar(self.rh, self.bgrt, 255, 255, ignore.nothing)
        cv2.createTrackbar(self.rr, self.bgrt, 20, 50, ignore.nothing)

        cv2.createTrackbar(self.hl, self.hsvt, 0, 179, ignore.nothing)
        cv2.createTrackbar(self.hh, self.hsvt, 179, 179, ignore.nothing)
        cv2.createTrackbar(self.hr, self.hsvt, 20, 50, ignore.nothing)
        cv2.createTrackbar(self.sl, self.hsvt, 0, 255, ignore.nothing)
        cv2.createTrackbar(self.sh, self.hsvt, 255, 255, ignore.nothing)
        cv2.createTrackbar(self.sr, self.hsvt, 20, 50, ignore.nothing)
        cv2.createTrackbar(self.vl, self.hsvt, 0, 255, ignore.nothing)
        cv2.createTrackbar(self.vh, self.hsvt, 255, 255, ignore.nothing)
        cv2.createTrackbar(self.vr, self.hsvt, 20, 50, ignore.nothing)

        cv2.createTrackbar(self.ll, self.labt, 0, 255, ignore.nothing)
        cv2.createTrackbar(self.lh, self.labt, 255, 255, ignore.nothing)
        cv2.createTrackbar(self.lr, self.labt, 20, 50, ignore.nothing)
        cv2.createTrackbar(self.al, self.labt, 0, 255, ignore.nothing)
        cv2.createTrackbar(self.ah, self.labt, 255, 255, ignore.nothing)
        cv2.createTrackbar(self.ar, self.labt, 20, 50, ignore.nothing)
        cv2.createTrackbar(self.bl, self.labt, 0, 255, ignore.nothing)
        cv2.createTrackbar(self.bh, self.labt, 255, 255, ignore.nothing)
        cv2.createTrackbar(self.byr, self.labt, 20, 50, ignore.nothing)

        cv2.createTrackbar(self.Yl, self.YCrCbt, 0, 255, ignore.nothing)
        cv2.createTrackbar(self.Yh, self.YCrCbt, 255, 255, ignore.nothing)
        cv2.createTrackbar(self.Yr, self.YCrCbt, 20, 50, ignore.nothing)
        cv2.createTrackbar(self.Crl, self.YCrCbt, 0, 310, ignore.nothing)
        cv2.createTrackbar(self.Crh, self.YCrCbt, 310, 310, ignore.nothing)
        cv2.createTrackbar(self.Crr, self.YCrCbt, 20, 50, ignore.nothing)
        cv2.createTrackbar(self.Cbl, self.YCrCbt, 0, 271, ignore.nothing)
        cv2.createTrackbar(self.Cbh, self.YCrCbt, 271, 271, ignore.nothing)
        cv2.createTrackbar(self.Cbr, self.YCrCbt, 20, 50, ignore.nothing)

    def pick_color_bgr(self, event, x, y, flags, param, image):
        if event == cv2.EVENT_LBUTTONDOWN:
            pixel = image[y, x]

            # HUE, SATURATION, AND VALUE (BRIGHTNESS) RANGES.
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

    def pick_color_hsv(self, event, x, y, flags, param, image):
        if event == cv2.EVENT_LBUTTONDOWN:
            pixel = image[y, x]

            # HUE, SATURATION, AND VALUE (BRIGHTNESS) RANGES.
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

    def pick_color_lab(self, event, x, y, flags, param, image):
        if event == cv2.EVENT_LBUTTONDOWN:
            pixel = image[y, x]

            # HUE, SATURATION, AND VALUE (BRIGHTNESS) RANGES.
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

    def pick_color_YCrCb(self, event, x, y, flags, param, image):
        if event == cv2.EVENT_LBUTTONDOWN:
            pixel = image[y, x]

            # HUE, SATURATION, AND VALUE (BRIGHTNESS) RANGES.
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

    def readTrackbars(self):
        # read trackbar positions for each trackbar

        self.bluel = cv2.getTrackbarPos(self.bl, self.bgrt)
        self.blueh = cv2.getTrackbarPos(self.bh, self.bgrt)
        self.bluer = cv2.getTrackbarPos(self.br, self.bgrt)
        self.greenl = cv2.getTrackbarPos(self.gl, self.bgrt)
        self.greenh = cv2.getTrackbarPos(self.gh, self.bgrt)
        self.greenr = cv2.getTrackbarPos(self.gr, self.bgrt)
        self.redl = cv2.getTrackbarPos(self.rl, self.bgrt)
        self.redh = cv2.getTrackbarPos(self.rh, self.bgrt)
        self.redr = cv2.getTrackbarPos(self.rr, self.bgrt)

        self.hul = cv2.getTrackbarPos(self.hl, self.hsvt)
        self.huh = cv2.getTrackbarPos(self.hh, self.hsvt)
        self.hur = cv2.getTrackbarPos(self.hr, self.hsvt)
        self.sal = cv2.getTrackbarPos(self.sl, self.hsvt)
        self.sah = cv2.getTrackbarPos(self.sh, self.hsvt)
        self.sar = cv2.getTrackbarPos(self.sr, self.hsvt)
        self.val = cv2.getTrackbarPos(self.vl, self.hsvt)
        self.vah = cv2.getTrackbarPos(self.vh, self.hsvt)
        self.var = cv2.getTrackbarPos(self.vr, self.hsvt)

        self.lightl = cv2.getTrackbarPos(self.ll, self.labt)
        self.lighth = cv2.getTrackbarPos(self.lh, self.labt)
        self.lightr = cv2.getTrackbarPos(self.lr, self.labt)
        self.g_rl = cv2.getTrackbarPos(self.al, self.labt)
        self.g_rh = cv2.getTrackbarPos(self.ah, self.labt)
        self.g_rr = cv2.getTrackbarPos(self.ar, self.labt)
        self.b_yl = cv2.getTrackbarPos(self.bl, self.labt)
        self.b_yh = cv2.getTrackbarPos(self.bh, self.labt)
        self.b_yr = cv2.getTrackbarPos(self.br, self.labt)

        self.lumal = cv2.getTrackbarPos(self.Yl, self.YCrCbt)
        self.lumah = cv2.getTrackbarPos(self.Yh, self.YCrCbt)
        self.lumar = cv2.getTrackbarPos(self.Yr, self.YCrCbt)
        self.Ycrl = cv2.getTrackbarPos(self.Crl, self.YCrCbt)
        self.Ycrh = cv2.getTrackbarPos(self.Crh, self.YCrCbt)
        self.Ycrr = cv2.getTrackbarPos(self.Crr, self.YCrCbt)
        self.YCbl = cv2.getTrackbarPos(self.Cbl, self.YCrCbt)
        self.Ycbh = cv2.getTrackbarPos(self.Cbh, self.YCrCbt)
        self.Ycbr = cv2.getTrackbarPos(self.Cbr, self.YCrCbt)

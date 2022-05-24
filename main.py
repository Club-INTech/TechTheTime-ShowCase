import cv2 as cv
import gpio
from const import *
from detection import detect_statue


if __name__ == "__main__":
    cap = cv.VideoCapture(2)

    while True:
        ret, frame = cap.read()
        x, xp = START_X_PIXEL, int(coeff*(START_X_PIXEL+STATUE_SIDE_PIXEL*(MEASURE_HEIGHT_CM / h)))
        y, yp = START_Y_PIXEL, int(coeff*(START_Y_PIXEL + STATUE_SIDE_PIXEL * (MEASURE_HEIGHT_CM / h)))
        crop = frame[x:xp, y:yp]
        cv.imshow('frame', crop)

        if detect_statue(crop):
            gpio.light_LED()
            break

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

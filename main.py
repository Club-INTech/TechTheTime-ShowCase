import cv2 as cv
from const import *
from detection import detect_statue

h = 34

if __name__ == "__main__":
    cap = cv.VideoCapture(2)

    while True:
        ret, frame = cap.read()
        x, xp = START_X_PIXEL, 2*int(START_X_PIXEL+STATUE_SIDE_PIXEL*(MEASURE_HEIGHT_CM / h))
        y, yp = START_Y_PIXEL, 2*int(START_Y_PIXEL + STATUE_SIDE_PIXEL * (MEASURE_HEIGHT_CM / h))
        crop = frame[x:xp, y:yp]
        cv.imshow('frame', crop)

        if detect_statue(crop):
            

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()
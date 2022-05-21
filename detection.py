from const import THRESHOLD


def detect_statue(frame):
    green_sum = 0
    pixel_num = len(frame) * len(frame[0])
    for i in range(frame.shape[0]):
        for j in range(frame.shape[1]):
            green_sum += frame[i][j][1]
    det = green_sum / pixel_num
    return det >= THRESHOLD

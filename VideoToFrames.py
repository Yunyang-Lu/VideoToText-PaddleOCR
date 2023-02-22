import cv2
import os
import threading

def VTF (video_path, outPutDirName, FPS):
    times = 0
    p_num = 0

    # if the path does not exist, create directory.
    if not os.path.exists(outPutDirName):
        os.makedirs(outPutDirName)

    # read the video
    video_capture = cv2.VideoCapture(video_path)

    # every frame_frequency frame will be saved
    frame_frequency = int(video_capture.get(cv2.CAP_PROP_FPS) / FPS)


    while True:
        times = times + 1
        res, image = video_capture.read()
        if not res:
            # print('not res , not image')
            break
        if times % frame_frequency == 0:
            p_num = p_num + 1
            cv2.imwrite(outPutDirName + '/' + str(p_num).zfill(3)+'.jpg', image)

    print('Converted to frames success')
    video_capture.release()

    return p_num

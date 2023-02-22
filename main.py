import cv2
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
import os
import paddle
import Polygon



from TextDetection import textDect

#from OCRTextExtractor import textExtractor
from VideoToFrames import VTF
#from ResultPic import saveOCRSample


if __name__ == "__main__":
 

    videoPath = "./Video/Video_Test14.mp4"
    FramesCache = "./FrameCache"
    OCRFrame = "./OCRFrame"

    os.makedirs(FramesCache, exist_ok=True)
    os.makedirs(OCRFrame, exist_ok=True)
    FPS_Needed = 0.5
    # frames needed to extract per second
    NumOfFrames = VTF(videoPath, FramesCache, FPS_Needed)


    det_model_dir="./inference/en_PP-OCRv3_det_infer/" 
    cls_model_dir="./inference/ch_ppocr_mobile_v2.0_cls_infer/" 
    rec_model_dir="./inference/en_PP-OCRv3_rec_infer/" 
    textDect(FramesCache, det_model_dir, cls_model_dir, rec_model_dir, OCRFrame)
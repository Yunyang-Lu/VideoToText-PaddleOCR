import os
import Polygon

def textDect (img_dir, det_dir, cls_dir, rec_dir, drawing_dir):
    #only detection
    '''
    os.system('python tools/infer/predict_det.py --image_dir="'+img_dir+'" \
            --det_model_dir="'+det_dir+'" \
            --draw_img_save_dir="'+drawing_dir+'" \
            --use_gpu=False')
    '''

    #'''
    os.system('python tools/infer/predict_system.py \
                    --image_dir="'+img_dir+'" \
                    --det_model_dir="'+det_dir+'" \
                    --cls_model_dir="'+cls_dir+'" \
                    --rec_model_dir="'+rec_dir+'" \
                    --rec_batch_num=6 \
                    --rec_char_dict_path=./ppocr/utils/en_dict.txt \
                    --use_space_char=True \
                    --use_angle_cls=False \
                    --draw_img_save_dir="'+drawing_dir+'" \
                    --use_gpu=False')
    #'''
    """
     --rec_batch_num=6 --max_text_length=25\
    """
from paddleocr import PaddleOCR


def textExtractor (img_path, lang):
    ocr = PaddleOCR(lang=lang, use_angle_cls=True)  # need to run only once to download and load model into memory

    result = ocr.ocr(img_path, cls=False)
    result = result[0]

    for line in result:
        print(line)

    return result
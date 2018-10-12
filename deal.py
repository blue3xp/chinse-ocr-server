from PIL import Image
import os
import ocr
import time
import shutil
import numpy as np
import  re
Uploadpic = './test_images/'
Createpic = 'static/createPic/'


def dealPicture(picSrc):
    print("picSrc:%s"%picSrc)
    result_dir = './test_result'
    if os.path.exists(result_dir):
        shutil.rmtree(result_dir)
    os.mkdir(result_dir)
    resultString = ""
    image_file = Uploadpic + picSrc
    print("image_file:%s"%image_file)
    image = np.array(Image.open(image_file).convert('RGB'))
    t = time.time()
    //利用原有模型实现识别
    result, image_framed = ocr.model(image)
    //利用pytesseract实现中文识别
    #result, image_framed = ocr.model2(image)
    output_file = os.path.join(result_dir, image_file.split('/')[-1])
    Image.fromarray(image_framed).save(output_file)
    print("Mission complete, it took {:.3f}s".format(time.time() - t))
    print("\nRecognition Result:\n")
    for key in result:
        print(result[key][1])
        resultString += result[key][1]
    resultString = re.sub("[#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~!]+", "",resultString)
    print("resultString:%s"%resultString)
    return resultString


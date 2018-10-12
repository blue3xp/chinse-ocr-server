#-*- coding:utf-8 -*-
import os
import ocr
import time
import shutil
import numpy as np
from PIL import Image
from glob import glob
import  re
image_files = glob('./test_images/*.*')


if __name__ == '__main__':
    result_dir = './test_result'
    if os.path.exists(result_dir):
        shutil.rmtree(result_dir)
    os.mkdir(result_dir)
    total = time.time()
    for image_file in sorted(image_files):
        print("image_file%s"%image_file)
        image = np.array(Image.open(image_file).convert('RGB'))
        t = time.time()
        #result, image_framed = ocr.model(image)
        result, image_framed = ocr.model2(image)
        output_file = os.path.join(result_dir, image_file.split('/')[-1])
        Image.fromarray(image_framed).save(output_file)
        print("Mission complete, it took {:.3f}s".format(time.time() - t))
        print("\nRecognition Result:\n")
        for key in result:
            result[key][1] = re.sub("[#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+!", "",result[key][1])
            print(result[key][1])
    print("finished complete, it took {:.3f}s".format(time.time() - total))

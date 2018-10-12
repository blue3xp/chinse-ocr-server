## 环境部署
``` Bash
sh setup.sh
```
## 运行
``` 
python manage.py 通过开启服务端 实现照片上传后识别
```



## 简介
基于Tensorflow和Keras pytesseract实现身份证识别，通过flask实现上传身份证图片，然后服务器识别后返回识别数据。


* 文本检测：CTPN
* 文本识别：DenseNet + CTC  tesseract

## 环境部署
``` Bash
sh setup.sh
```
* 注：CPU环境执行前需注释掉for gpu部分，并解开for cpu部分的注释

## Demo
将测试图片放入test_images目录，检测结果会保存到test_result中

``` Bash
python demo.py 控制台离线识别
```

## 模型训练

### CTPN训练
详见ctpn/README.md

### DenseNet + CTC训练

#### 1. 数据准备

数据集：https://pan.baidu.com/s/1QkI7kjah8SPHwOQ40rS1Pw (密码：lu7m)
* 共约364万张图片，按照99:1划分成训练集和验证集
* 数据利用中文语料库（新闻 + 文言文），通过字体、大小、灰度、模糊、透视、拉伸等变化随机生成
* 包含汉字、英文字母、数字和标点共5990个字符
* 每个样本固定10个字符，字符随机截取自语料库中的句子
* 图片分辨率统一为280x32

图片解压后放置到train/images目录下，描述文件放到train目录下

#### 2. 训练

``` Bash
cd train
python train.py
```

#### 3. 结果

| val acc | predict | model |
| -----------| ---------- | -----------|
| 0.983 | 8ms | 18.9MB |

* GPU: GTX TITAN X
* Keras Backend: Tensorflow

#### 4. 生成自己的样本

可参考[SynthText_Chinese_version](https://github.com/JarveeLee/SynthText_Chinese_version)，[TextRecognitionDataGenerator](https://github.com/Belval/TextRecognitionDataGenerator)和[text_renderer](https://github.com/Sanster/text_renderer)



## 参考

[1] https://github.com/eragonruan/text-detection-ctpn

[2] https://github.com/senlinuc/caffe_ocr

[3] https://github.com/chineseocr/chinese-ocr

[4] https://github.com/xiaomaxiao/keras_ocr



http://www.cnblogs.com/hutao722/p/9564456.html
https://www.jianshu.com/p/fa204a54a956?from=singlemessage
https://github.com/MPIG-Robot/Mobile-DeepLearning-in-TensorFlow-Lite


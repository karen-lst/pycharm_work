from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random

im = Image.open('0.jpg')

# 缩放50%
# w, h = im.size
# print('size: %s*%s' % (w,h))
# im.thumbnail((w // 2, h // 2))
# print('size: %s*%s' % (w // 2, h // 2))
# im.save('thumbnali.jpg', 'jpeg')

# 应用模糊滤镜
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('bulr.jpg', 'jpeg')

# 生成字母验证码图片
# 生成随机数字，用chr()方法把数字转换成字母，大写字母65-90，小写字母97-122
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1，产生随机的
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
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

# 随机颜色1，产生（64,255）之间随机的三个数字，并返回
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))


def rndcolor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))


width = 60*4
height = 60

# 创建图像对象 Image.new(mode,size,color)
image = Image.new('RGB',(width,height),(255,255,255))
# 创建 Font 对象
font = ImageFont.truetype('Arial.ttf',36)
# 创建 Draw 对象
draw = ImageDraw.Draw(image)
# 填充image的每一个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y), fill=rndColor())
# 输出文字
for i in range(4):
    draw.text((60*i+10,10),rndChar(),font=font,fill=rndcolor2())
# 对图像模糊处理
image.filter(ImageFilter.BLUR)
# 保存图像
image.save('1.jpg','jpeg')
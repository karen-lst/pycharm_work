from PIL import Image, ImageDraw, ImageFont

im = Image.open('thumbnali.jpg')
w, h = im.size
im.thumbnail((w // 4, h // 4))
print(im.size)
draw = ImageDraw.Draw(im)
font = ImageFont.truetype('Arial.ttf', 30)
draw.text((185, -5), '4', font=font, fill='red')

im.save('t1.jpg', 'jpeg')

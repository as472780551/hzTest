# -*- coding: UTF-8 -*-
import cv2
import ft2

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


img = cv2.imread('pic/lena.jpg')
line = '你好,我是 lena'

color = (0, 255, 0)  # Green
pos = (3, 3)
text_size = 24

# ft = put_chinese_text('wqy-zenhei.ttc')
ft = ft2.put_chinese_text('msyh.ttf')
image = ft.draw_text(img, pos, line, text_size, color)

name = u'图片展示'

cv2.imshow(name, image)
cv2.waitKey(0)

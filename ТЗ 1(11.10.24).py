import pyqrcode
import png

a = input('Какой текст хотите преобпазовать в QR-код?')
s = input('Какое будет название файла?')
d = int(input('Какой будет размер картинки?'))

my_qr = pyqrcode.create(a)
my_qr.png(s + '.png', scale = d)
print('QR-код сгенерирован')
print(my_qr.text())


import qrcode

qr = qrcode.make('hello word')
qr.save('myQR.png')
from MyQR import myqr

version, level, qr_name = myqr.run(
    words = 'Correct nice qr code',
    version = 2,
    level = 'H',
    picture = 'banner3.jpg',
    colorized=True,
    contrast=1.0,
    brightness = 1.0,
    save_name='generate.png',

)
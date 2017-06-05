# coding=UTF-8

# get all the kind of phone num which is divided as 3-4-4
# check with 3-4 to get the phone's msg from net
# with this we can serve the customer better
# 17-05-02 haining.qin changhong

# ENVIRONMENT: python2.7

# get provider information by phoneNumber

import sys
import os

def run_example(data="http://www.lincolnloop.com", *args, **kwargs):
    """
    Build an example QR Code and display it.
    There's an even easier way than the code here though: just use the ``make``
    shortcut.
    """
    import qrcode
    qr = qrcode.QRCode(*args, **kwargs)
    qr.add_data(data)
    im = qr.make_image()
    print('im.show')
    echo(im)
    im.show()

run_example()
#            print Date().time

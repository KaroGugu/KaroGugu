import pygrcode
import png
from pygrcode import QRCode

link = 'https://www.forbes.com/sites/jimgorzelany/2019/07/23/here-are-the-coolest-new-cars-for-2020/'
url = pygrcode.create(link)
url.png('qr.png', scale=8)

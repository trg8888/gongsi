from PIL import Image
from resizeimage import resizeimage
from io import BytesIO
import redis
import uuid
from model import Quantity,db
from io import StringIO,BytesIO
import requests
def ceshi():
    comtt = requests.get('https://m.media-amazon.com/images/I/61c7UVUWnlL._AC_UX466_.jpg').content

    name = uuid.uuid4().hex
    img = Image.open(BytesIO(comtt))
    bytesIO = BytesIO()
    img = resizeimage.resize_contain(img, [800, 800])
    img.save(bytesIO, format='PNG')
    r = redis.StrictRedis(host='localhost')
    r.lpush(name,bytesIO.getvalue())
    # fd_img.close()
    name_ = Quantity(
        name = name,
        description = 'description',
        attribute = 'attribute',
        picture = name,
        price = '96',
        book_id = '1'
    )
    db.session.add(name_)
    db.session.commit()

for i in range(100):
    ceshi()
# with open('666.jpg', 'r+b') as f:
#     with Image.open(f) as image:
#         cover = resizeimage.resize_cover(image, [200, 100])
#         cover.save('test-image-cover.jpeg', image.format)
# r = redis.StrictRedis(host='localhost')
# imgs = r.lrange('ae7d6a02986b4cb6a078bc93c0331c31',0,-1)
# for img in imgs:
#     img = Image.open(BytesIO(img))
#     img.save('666.jpg', format='PNG')

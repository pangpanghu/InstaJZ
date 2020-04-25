from django.db import models
from imagekit.models import ProcessedImageField
try:
    from PIL import Image
except ImportError:
    import Image

# Create your models here. 定义自己的model 就是定义数据结构和类，然后后面还要和数据进行匹配
# Post 类下面两个数据段，各是什么结构， 导入的PostImageField这个里面有现成的类， 但不知道这个 upload_to的路径是什么时候定义的

class Post (models.Model):
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField (
        upload_to= 'static/images/posts',
        format= 'JPEG',
        options={'quality': 100},
        blank= True,
        null= True,
    )

    # image 可以是Blank 也可以是Null



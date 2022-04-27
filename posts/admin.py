from django.contrib import admin

# Register your models here.
from .models import Posts
admin.site.register(Posts)

from .models import Categories
admin.site.register(Categories)

from .models import Mosts
admin.site.register(Mosts)

from .models import Tosts
admin.site.register(Tosts)

from .models import Poster
admin.site.register(Poster)
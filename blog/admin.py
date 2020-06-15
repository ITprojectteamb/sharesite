from django.contrib import admin
from .models import Post,Give,Want,Profile

admin.site.register(Post)
admin.site.register(Give)
admin.site.register(Want)

##################################################################
#ここから先追加箇所＃
##################################################################

admin.site.register(Profile)
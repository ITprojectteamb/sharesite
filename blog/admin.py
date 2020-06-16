from django.contrib import admin
from .models import Post,Give,Want,Profile,Item,Employee,Give_info,Give_comment,Want_info,Want_comment

admin.site.register(Post)
admin.site.register(Give)
admin.site.register(Want)

##################################################################
#ここから先追加箇所＃
##################################################################

admin.site.register(Profile)
admin.site.register(Item)
admin.site.register(Employee)
admin.site.register(Give_info)
admin.site.register(Give_comment)
admin.site.register(Want_info)
admin.site.register(Want_comment)  

from django.contrib import admin

from .models import Post,Give,Want,Profile,Item,Employee,Give_comment,Want_comment

admin.site.register(Post)
admin.site.register(Give)
admin.site.register(Want)
admin.site.register(Profile)
admin.site.register(Item)
admin.site.register(Employee)
admin.site.register(Give_comment)
admin.site.register(Want_comment)  

from django.contrib import admin

from .models import Give,Want,Profile,Give_comment,Want_comment,Profile_comment

admin.site.register(Give)
admin.site.register(Want)
admin.site.register(Profile)
admin.site.register(Give_comment)
admin.site.register(Want_comment)  
admin.site.register(Profile_comment)  
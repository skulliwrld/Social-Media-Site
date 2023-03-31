from django.contrib import admin
from. models import profile, Post,Likepost,FellowerCount

# Register your models here.
admin.site.register(profile)
admin.site.register(Post)
admin.site.register(Likepost)
admin.site.register(FellowerCount)

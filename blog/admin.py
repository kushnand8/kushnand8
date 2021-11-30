from django.contrib import admin
from .models import AddPost,AddComment,ContactUs
# Register your models here.
@admin.register(AddPost)
class AddPostModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','pst']


@admin.register(AddComment)
class AddCommentModelAdmin(admin.ModelAdmin):
    list_display=['comment','post']

@admin.register(ContactUs)
class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','desc']
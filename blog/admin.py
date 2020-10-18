from django.contrib import admin

# Register your models here.
from .models import Post
# to import the previously made model
admin.site.register(Post) # to make the model visile on the admin page

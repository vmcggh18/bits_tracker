from django.contrib import admin
from .models import Item, Votefor, Comment
from .models import *

# Register your models here.
admin.site.register(Item)
admin.site.register(Votefor)
admin.site.register(Comment)

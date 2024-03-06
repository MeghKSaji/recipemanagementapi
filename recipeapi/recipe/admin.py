from django.contrib import admin

from recipe.models import Recipe,Review_or_Comment

# Register your models here.


admin.site.register(Recipe)
admin.site.register(Review_or_Comment)


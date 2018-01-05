from django.contrib import admin

from .models import blogs

class blogsModelAdmin(admin.ModelAdmin):
	list_display = ["title", "desc"]


	search_fields = ["title", "desc"]
	class Meta:
		model = blogs


admin.site.register(blogs, blogsModelAdmin)

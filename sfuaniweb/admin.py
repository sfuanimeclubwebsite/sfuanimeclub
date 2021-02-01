from django.contrib import admin
from .models import news_post,events,administration,about,event_countdown, gallery,screenings,index_cover

# Register your models here.
admin.site.register(news_post)
admin.site.register(events)
admin.site.register(gallery)
admin.site.register(administration)
admin.site.register(index_cover)
admin.site.register(about)
admin.site.register(screenings)
admin.site.register(event_countdown)

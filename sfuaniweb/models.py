from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

#www.facebook.com/sfuanimeclub/

class news_post(models.Model):
    title = models.CharField(max_length=255, help_text="Title of blog posting")
    cover_image = models.ImageField(upload_to='img/cover/', default='img/cover/logo.jpg')
    body = RichTextUploadingField(blank=True, null=True)
    datetime = models.DateField()
    body_alt = models.CharField(max_length=255, help_text="Title of blog posting",null=True)

    pinned = models.BooleanField(default=False,blank=True,null=False)
    author = models.CharField(max_length=255, help_text="Author", default="SFU Exec Team")
    tag = models.CharField(max_length=255, help_text="Topic of photo")

class index_cover(models.Model):
    title = models.CharField(max_length=255, help_text="Title of cover image")
    cover_image = models.ImageField(upload_to='img/cover/', default='img/cover/logo.jpg')
    body = RichTextUploadingField(blank=True, null=True)
    link = models.CharField(max_length=255, help_text="Id number that links to the webpage")
    body_alt = models.CharField(max_length=255, help_text="Title of blog posting",null=True)

class events(models.Model):
    title = models.CharField(max_length=255, help_text="event")

    body = RichTextUploadingField(blank=True, null=True)
    datetime = models.DateField()

class administration(models.Model):
    title = models.CharField(max_length=255, help_text="admin")

    body = RichTextUploadingField(blank=True, null=True)
    datetime = models.DateField()

class gallery(models.Model):
    title = models.CharField(max_length=255, help_text="name of photo")
    hotel_Main_Img = models.ImageField(upload_to='img/index-gallery/')
    datetime = models.DateField()
    tag = models.CharField(max_length=255, help_text="Topic of photo")


class about(models.Model):
    title = models.CharField(max_length=255, help_text="about")
    body = RichTextUploadingField(blank=True, null=True)
    datetime = models.DateField()

class screenings(models.Model):

    title = models.CharField(max_length=255, help_text="Name of screening")
    time_location = models.CharField(max_length=255, help_text="When and where?")
    body = RichTextUploadingField(blank=True, null=True)
    hotel_Main_Img = models.ImageField(upload_to='img/screens/')
    datetime = models.DateField()

class event_countdown(models.Model):
    title = models.CharField(max_length=255, help_text="Name of event")
    cover_image = models.ImageField(upload_to='img/cover/', default='img/cover/logo.jpg')
    datetime = models.DateField()

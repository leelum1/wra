from django.db import models
from django.core.urlresolvers import reverse
from markdownx.models import MarkdownxField
from asset_app.models import User

class Book(models.Model):
    STATUS = (
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
        ('Reference', 'Reference'),
    )

    title = models.CharField(max_length=512, unique=True)
    author = models.CharField(max_length=225, blank=True, null=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=225, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    isbn = models.CharField(max_length=80, blank=True, null=True)
    status = models.CharField(max_length=80, choices=STATUS)
    uploaddate = models.DateTimeField(auto_now_add=True)
    bookcover = models.FileField(upload_to='documents/covers/', blank=True, null=True, max_length=225)
    document = models.FileField(upload_to='documents/', blank=True, null=True, max_length=225)

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('library_app:book-detail',kwargs={'pk':self.id})

    def __str__(self):
        return self.title


class BookRequest(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now=True)
    request_fullfilled = models.BooleanField(default=False)

    def __str__(self):
        return self.book.title + " by " + self.User.first_name + " " + self.User.last_name


class SOP(models.Model):
    CATEGORY = (
        ('general', 'General'),
        ('rainfall', 'Rainfall'),
        ('streamflow', 'Streamflow'),
        ('groundwater', 'Groundwater'),
        ('quality', 'Water Quality'),
        ('gis', 'GIS'),
    )
    title = models.CharField(max_length=225)
    slug = models.SlugField()
    description = models.TextField()
    category = models.CharField(max_length=125, choices=CATEGORY)
    text = MarkdownxField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('library_app:sop-detail',kwargs={'slug':self.slug})

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.

# Create a Blog model
# - title
# - pub_date (publication date)
# - body
# - image
class Blog(models.Model):
  title = models.CharField(max_length=225)
  pubDate = models.DateTimeField()
  body = models.TextField()
  image = models.ImageField(upload_to='images/')

# Add Blog app to settings

# Create a migration

# Migrate

# Add to the admin
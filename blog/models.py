"""Blog model for database definition"""

from django.db import models

# Create your models here.

# Create a Blog model
# - title
# - pub_date (publication date)
# - body
# - image

class Blog(models.Model):
  """This class is a Blog model definition"""
  title = models.CharField(max_length=225)
  pub_date = models.DateTimeField()
  body = models.TextField()
  image = models.ImageField(upload_to='images/')

  def __str__(self):
    """Show the blog title in admin dashboard"""
    return self.title

  def summary(self):
    """This method returns a shortened version of the body"""
    return self.body[:100]

  def pub_date_pretty(self):
    """Prettify published date to M/D/YYYY"""
    return self.pub_date.strftime('%b %e %Y')

# Add Blog app to settings

# Create a migration

# Migrate

# Add to the admin

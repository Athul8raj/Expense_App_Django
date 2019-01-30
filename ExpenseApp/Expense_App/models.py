from django.db import models
from django.utils import timezone
from .util import get_current_user
from django.contrib.auth.models import User
import os

class Expenses(models.Model):
    exp_name = models.CharField(max_length=80)
    total_price = models.CharField(max_length=50)
    date_uploaded = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='documents/',default='media/documents/dog.jpg',null=True)
    
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, editable=False, related_name='%(class)s_created')
    modified_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, editable=False, related_name='%(class)s_modified')

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user:
            self.modified_by = user
            if not self.id:
                self.created_by = user
        super(Expenses, self).save(*args, **kwargs)
        
    def get_absolute_image(self):
        return os.path.join('/media/', self.image.name)
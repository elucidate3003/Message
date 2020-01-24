from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
def upload_image(instance,filename):
    return f'{instance.user}/{filename}'


def upload(instance,filename):
    return f'{instance.caption}/{filename}'

class Home(models.Model):
    caption = models.CharField(_("Caption"), max_length=50, blank=True, null=True)
    image = models.ImageField(_("Image"), upload_to='post/',  max_length=None, blank=True, null=True)
        
    def __str__(self):
        return self.caption

class Message(models.Model):
    post = models.ForeignKey(Home, verbose_name=_("Post"), on_delete=models.CASCADE, blank=True, null=True)
    user = models.CharField(_("User"), max_length=50, blank=True, null=True)
    message = models.TextField(_("Message"), blank=True, null=True)
    photo = models.ImageField(_("Image"), upload_to='message/', max_length=None, blank=True, null=True)
    
    def __str__(self):
        return self.user

    




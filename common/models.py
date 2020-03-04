from django.db import models

# Create your models here.


class Menu(models.Model):

    menu_name = models.CharField(max_length=10, verbose_name=u'菜单名', null=False, blank=False)
    menu_url = models.CharField(max_length=30, verbose_name=u'菜单URL', null=True, blank=True)
    menu_icon = models.CharField(max_length=30, verbose_name=u'菜单图标', null=True, blank=True)
    parent_id = models.CharField(max_length=11, verbose_name=u'父菜单ID', null=True, blank=True)
    menu_level = models.IntegerField(verbose_name=u'菜单级别',  default=1, null=False, blank=False)

    def __unicode__(self):
        return '{}-{}'.format(self.menu_name, self.menu_url)

from django.db import models
from django.urls import reverse_lazy

class Service(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    image = models.ImageField('Фото', upload_to='images')
    text = models.TextField('Описание')
    price = models.IntegerField('Цена',default=0)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse_lazy('service_detail', kwargs={'service_id':self.pk})

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

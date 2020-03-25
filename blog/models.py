from django.db import models
from django.utils import timezone


class Post(models.Model):
    #Post modelimizin ismi. Başka bir isim de verebilirdik (yeter ki özel karakterler ve boşluk kullanmayalım). class isimleri her zaman büyük harf ile başlamalıdır.
    #models.Model Post'un bir Django Modeli olduğunu belirtir, bu şekilde Django onu veritabanında tutması gerektiğini bilir.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #models.ForeignKey - başka bir modele referans tanımlar.
    title = models.CharField(max_length=200)
    #models.CharField - belirli bir uzunluktaki metinleri tanımlamak için kullanılır.
    text = models.TextField()
    #models.TextField - bu da uzun metinleri tanımlar. Blog gönderileri için biçilmiş kaftan, değil mi?
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        #publish metodu. def bunun bir fonksiyon/method olduğunu söylüyor. publish ise methodumuzun ismi. 
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

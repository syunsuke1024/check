from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = "user"
        verbose_name = "user"
        verbose_name_plural ="user"

    user_name = models.CharField(max_length=100,unique=True,verbose_name="user_name")

    def __str__(self):
        return self.user_name

class Links(models.Model):
    class Meta:
        db_table = "links"
        verbose_name = "リンク集"
        verbose_name_plural ="リンク集"

    priority = models.IntegerField(verbose_name="重要度",help_text="整数を入力してください")
    link = models.CharField(max_length=255,verbose_name="リンク先")
    memo = models.CharField(max_length=255,blank=True,verbose_name="備考")
    user = models.ForeignKey(User,on_delete=models.PROTECT,verbose_name="USER")

    def __str__(self):
        return self.memo

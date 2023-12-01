from django.db import models

# Create your models here.
from accounts.models import CustomUser
    
class SnsappPost(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )

    comment = models.CharField(
        verbose_name='文章',
        max_length=140
    )

    image1 = models.ImageField(
        verbose_name='イメージ1',
        upload_to='photos',
        blank=True,
        null=True
    )
    image2 = models.ImageField(
        verbose_name='イメージ2',
        upload_to='photos',
        blank=True,
        null=True
    )
    image3 = models.ImageField(
        verbose_name='イメージ3',
        upload_to='photos',
        blank=True,
        null=True
    )
    image4 = models.ImageField(
        verbose_name='イメージ4',
        upload_to='photos',
        blank=True,
        null=True
    )
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )
    def __str__(self):
        return self.comment
    
class Like(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        SnsappPost,
        verbose_name='カテゴリ',
        on_delete=models.CASCADE
    )

class FollowUser(models.Model):
    followee = models.ForeignKey(
        CustomUser,
        verbose_name='被フォロー',
        on_delete=models.CASCADE,
        related_name='followee_set',
    )

    follower = models.ForeignKey(
        CustomUser,
        verbose_name='フォロワー',
        on_delete=models.CASCADE,
        related_name='follower_set'
    )
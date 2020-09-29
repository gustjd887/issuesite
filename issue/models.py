from django.db import models


class Community(models.Model):
    site = models.CharField(max_length=10)
    rank = models.CharField(max_length=100)

    def __str__(self):
        return self.site


class Issue(models.Model):
    site = models.ForeignKey(Community, max_length=10, on_delete=models.CASCADE)
    url = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=100)  # 제목
    reply = models.IntegerField()  # 댓글
    name = models.CharField(max_length=30)  # 닉네임 및 아이디
    date = models.DateTimeField()  # 원본 작성 시간
    hit = models.IntegerField()  # 조회수
    like = models.IntegerField()  # 추천 및 좋아요

    def __str__(self):
        return self.title

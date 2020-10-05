from django.db import models
from django.contrib.postgres.fields import ArrayField


site_choice = (('pp', '뽐뿌'), ('cl', '클리앙'), ('ou', '오유')) # 선택할 수 있는 커뮤니티 목록 정의


class Community(models.Model):
    site = models.CharField(max_length=10, choices=site_choice) # 전체 랭킹을 위한 total이 추가되어 있으며, 이후 선택은 3가지중 하나
    rank = models.CharField(max_length=200) # 랭킹을 나열. Issue 클래스의 id를 저장한다.

    def __str__(self):
        return self.site


class Issue(models.Model):
    site = models.ForeignKey(Community, max_length=10, on_delete=models.CASCADE, choices=site_choice) # 커뮤니티 이름
    url = models.CharField(max_length=200, unique=True) # 주소
    title = models.CharField(max_length=100)  # 제목
    reply = models.IntegerField()  # 댓글
    name = models.CharField(max_length=30)  # 닉네임 및 아이디
    date = models.DateTimeField()  # 원본 작성 시간
    hit = models.IntegerField()  # 조회수
    like = models.IntegerField()  # 추천 및 좋아요

    def __str__(self):
        return self.title

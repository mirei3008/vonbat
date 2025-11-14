from django.db import models

# 求人情報を表すモデル
# 1件の求人（職種・会社名・勤務地・仕事内容・掲載日）をデータベースで管理する

class Job(models.Model):
    # 職種名（例：エンジニア、営業など）
    title = models.CharField("職種", max_length=100)

    # 会社名
    company = models.CharField("会社名", max_length=100)

    # 勤務地（空欄可）
    location = models.CharField("勤務地", max_length=100, blank=True)

    # 仕事内容（空欄可、長文対応）
    description = models.TextField("仕事内容", blank=True)

    # 掲載日（求人が登録された日時、自動セット）
    posted_at = models.DateTimeField("掲載日", auto_now_add=True)

    class Meta:
        # デフォルトの並び順（新着順、ID降順）
        ordering = ("-posted_at", "-id")

    def __str__(self):
        # 管理画面や一覧表示用の文字列
        return f"{self.title} @ {self.company}"

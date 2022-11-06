from django.db import models

class Music(models.Model):
    TR='TR'
    TN='TN'
    HS='HS'
    EL='EL'
    AM='AM'
    DB='DB'
    ND='ND'
    STYLE_CHOICES=[
        (TR,'trance'),
        (TN,'techno'),
        (HS,'house'),
        (EL,'electro'),
        (AM,'ambient'),
        (DB,'dnb'),
        (ND,'nudisco')
    ]

    title=models.CharField(max_length=20)
    content=models.TextField(blank=True)
    audio=models.FileField(upload_to='media/')
    style=models.CharField(max_length=2,choices=STYLE_CHOICES, default=HS)

    def __str__(self):
        return f'{self.title}: {self.content}.'

class SubMusic(models.Model):
    style=models.CharField(max_length=20, blank=True)
    sub_style=models.CharField(max_length=120)
    representative=models.TextField(blank=True)

    def __str__(self):
        return f'Подстили {self.style}: {self.sub_style}. Представители стиля: {self.representative}'
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='職種')),
                ('company', models.CharField(max_length=100, verbose_name='会社名')),
                ('location', models.CharField(blank=True, max_length=100, verbose_name='勤務地')),
                ('description', models.TextField(blank=True, verbose_name='仕事内容')),
                ('posted_at', models.DateTimeField(auto_now_add=True, verbose_name='掲載日')),
            ],
            options={'ordering': ('-posted_at','-id')},
        )
    ]

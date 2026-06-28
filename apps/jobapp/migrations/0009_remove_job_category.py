from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('jobapp', '0008_alter_job_category_delete_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='category',
        ),
    ]


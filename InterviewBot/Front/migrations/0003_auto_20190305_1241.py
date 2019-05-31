# Generated by Django 2.1.7 on 2019-03-05 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0002_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='Category',
            field=models.CharField(choices=[('HR', 'HR'), ('TECHNICAL', 'TECHNICAL'), ('GK', 'GK'), ('Reading books', 'Reading books'), ('reading novels', 'reading novels'), ('Cooking', 'Cooking'), ('Watching Movies', 'Watching Movies'), ('Playing Badminton', 'Playing Badminton'), ('Playing Cricket', 'Playing Cricket'), ('Playing football', 'Playing football'), ('Playing basketball', 'Playing basketball'), ('Playing Chess', 'Playing Chess'), ('Going Gym', 'Going Gym'), ('listening Music', 'listening Music'), ('Dancing', 'Dancing'), ('C++', 'C++'), ('C', 'C'), ('JAVA', 'JAVA'), ('C#', 'C#'), ('.NET', '.NET'), ('PYTHON', 'PYTHON'), ('JavaScript', 'JavaScript'), ('HTML', 'HTML'), ('CSS', 'CSS'), ('Database', 'Database'), ('Networking', 'Networking'), ('Cloud', 'Cloud'), ('Android', 'Android'), ('Machine learning', 'ML'), ('AI', 'AI'), ('Data science', 'Data science')], max_length=50),
        ),
    ]

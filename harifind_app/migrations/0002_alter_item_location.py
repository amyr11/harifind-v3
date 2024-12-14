# Generated by Django 5.1.4 on 2024-12-14 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harifind_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='location',
            field=models.CharField(choices=[('Gusaling Aquino', 'Gusaling Aquino'), ('Gusaling Atienza', 'Gusaling Atienza'), ('Gusaling Bagatsing', 'Gusaling Bagatsing'), ('Gusaling Ejercito', 'Gusaling Ejercito'), ('Gusaling Katipunan', 'Gusaling Katipunan'), ('Gusaling Lacson', 'Gusaling Lacson'), ('Gusaling Villegas', 'Gusaling Villegas'), ('Entrepreneurial Building', 'Entrepreneurial Building'), ('Executive Building', 'Executive Building'), ('Flame Torch', 'Flame Torch'), ('Justo Albert Auditorium', 'Justo Albert Auditorium'), ('Mini Garden', 'Mini Garden'), ('Parking Space', 'Parking Space'), ('PLM Catwalk', 'Plm Catwalk'), ('PLM Chapel', 'Plm Chapel'), ('PLM Field', 'Plm Field'), ('Pride Hall', 'Pride Hall'), ('Rajah Sulayman Gym', 'Rajah Sulayman Gym'), ('Study Gazebo', 'Study Gazebo'), ('Tanghalang Bayan', 'Tanghalang Bayan'), ('University Activity Center', 'University Activity Center'), ('University Canteen', 'University Canteen'), ('University Library', 'University Library')], max_length=100),
        ),
    ]

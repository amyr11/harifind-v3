from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to="profile_images/", null=True, blank=True)
    year_level = models.IntegerField(null=True, blank=True)


# Create your models here.
class Item(models.Model):
    class Category(models.TextChoices):
        PERSONAL = "Personal Items"
        SCHOOL = "School Items"
        ELECTRONICS = "Electronics"
        EDUCATIONAL = "Books and Educational Items"
        SPORTS = "Sports Items"
        FOODANDDRINK = "Food and Drink Containers"
        MISCELLANEOUS = "Miscellaneous"
        IDENTIFICATION = "Identification and Documents"

    class Location(models.TextChoices):
        GUSALING_AQUINO = "Gusaling Aquino"
        GUSALING_ATIENZA = "Gusaling Atienza"
        GUSALING_BAGATSING = "Gusaling Bagatsing"
        GUSALING_EJERCITO = "Gusaling Ejercito"
        GUSALING_KATIPUNAN = "Gusaling Katipunan"
        GUSALING_LACSON = "Gusaling Lacson"
        GUSALING_VILLEGAS = "Gusaling Villegas"
        ENTREPRENEURIAL_BUILDING = "Entrepreneurial Building"
        EXECUTIVE_BUILDING = "Executive Building"
        FLAME_TORCH = "Flame Torch"
        JUSTO_ALBERT_AUDITORIUM = "Justo Albert Auditorium"
        MINI_GARDEN = "Mini Garden"
        PARKING_SPACE = "Parking Space"
        PLM_CATWALK = "PLM Catwalk"
        PLM_CHAPEL = "PLM Chapel"
        PLM_FIELD = "PLM Field"
        PRIDE_HALL = "Pride Hall"
        RAJAH_SULAYMAN_GYM = "Rajah Sulayman Gym"
        STUDY_GAZEBO = "Study Gazebo"
        TANGHALANG_BAYAN = "Tanghalang Bayan"
        UNIVERSITY_ACTIVITY_CENTER = "University Activity Center"
        UNIVERSITY_CANTEEN = "University Canteen"
        UNIVERSITY_LIBRARY = "University Library"

    class Type(models.TextChoices):
        LOST = "Lost"
        FOUND = "Found"

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reported_items", null=True
    )
    type = models.CharField(choices=Type.choices, max_length=100)
    image = models.ImageField(upload_to="item_images/")
    name = models.CharField(max_length=100)
    category = models.CharField(choices=Category.choices, max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(choices=Location.choices, max_length=100)
    returned = models.BooleanField(default=False)
    returned_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="returned_items",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        null=True,
        related_name="comments",
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        length = 20
        return (
            self.comment[:length] + "..."
            if len(self.comment) > length
            else self.comment
        )

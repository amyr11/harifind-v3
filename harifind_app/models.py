from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Degree(models.TextChoices):
        CED_BECEd = "CED_BECEd", "Bachelor of Early Childhood Education (BECEd)"
        CED_BEEd_PSE = (
            "CED_BEEd_PSE",
            "Bachelor of Elementary Education with Specialization in Pre-School Education (BEEd-PSE)",
        )
        CED_BPE_SPE = (
            "CED_BPE_SPE",
            "Bachelor of Physical Education major in School Physical Education (BPE-SPE)",
        )
        CED_BSEd_Eng = (
            "CED_BSEd_Eng",
            "Bachelor of Secondary Education with Specialization in English (BSEd Eng)",
        )
        CED_BSEd_Fil = (
            "CED_BSEd_Fil",
            "Bachelor of Secondary Education with Specialization in Filipino (BSEd Fil)",
        )
        CED_BSEd_Math = (
            "CED_BSEd_Math",
            "Bachelor of Secondary Education with Specialization in Mathematics (BSEd Math)",
        )
        CED_BSEd_Sci = (
            "CED_BSEd_Sci",
            "Bachelor of Secondary Education with Specialization in Science (BSEd Sci)",
        )
        CED_BSEd_SS = (
            "CED_BSEd_SS",
            "Bachelor of Secondary Education major in Social Studies (BSEd SS)",
        )
        SOG_BPA = "SOG_BPA", "Bachelor of Public Administration (BPA)"
        PROFESSIONAL_LAWS = "PROFESSIONAL_LAWS", "Bachelor of Laws (now Juris Doctor)"
        PROFESSIONAL_MEDICINE = "PROFESSIONAL_MEDICINE", "Doctor of Medicine"
        PROFESSIONAL_MA_EDUCATION = (
            "PROFESSIONAL_MA_EDUCATION",
            "Master of Arts in Education: Educational Administration, Social Studies, Biological Sciences, and Physical Sciences",
        )
        PROFESSIONAL_MA_PSYCHOLOGY = (
            "PROFESSIONAL_MA_PSYCHOLOGY",
            "Master of Arts in Psychology: Industrial Psychology, and Clinical Psychology",
        )
        PROFESSIONAL_MA_COMMUNICATION = (
            "PROFESSIONAL_MA_COMMUNICATION",
            "Master of Arts in Communication Management",
        )
        PROFESSIONAL_MA_PRINCIPALSHIP = (
            "PROFESSIONAL_MA_PRINCIPALSHIP",
            "Master of Arts in School Principalship",
        )
        PROFESSIONAL_M_FAMILY_SCIENCE = (
            "PROFESSIONAL_M_FAMILY_SCIENCE",
            "Master in Family Science",
        )
        PROFESSIONAL_MS_MATH_EDUCATION = (
            "PROFESSIONAL_MS_MATH_EDUCATION",
            "Master of Science in Mathematics Education",
        )
        PROFESSIONAL_EDD_EDUCATIONAL_ADMIN = (
            "PROFESSIONAL_EDD_EDUCATIONAL_ADMIN",
            "Doctor of Education in Educational Administration",
        )
        PROFESSIONAL_ME_ENGINEERING = (
            "PROFESSIONAL_ME_ENGINEERING",
            "Master of Engineering - with Specializations in: Structural Engineering, Computer Engineering, and Construction Management",
        )
        PROFESSIONAL_MS_ICT = (
            "PROFESSIONAL_MS_ICT",
            "Master of Science in Information and Communications Technology",
        )
        PROFESSIONAL_MS_MANAGEMENT_ENGINEERING = (
            "PROFESSIONAL_MS_MANAGEMENT_ENGINEERING",
            "Master of Science in Management Engineering",
        )
        PROFESSIONAL_MA_NURSING = "PROFESSIONAL_MA_NURSING", "Master of Arts in Nursing"
        PROFESSIONAL_M_LAWS = "PROFESSIONAL_M_LAWS", "Master of Laws"
        PROFESSIONAL_BBM_MBA = (
            "PROFESSIONAL_BBM_MBA",
            "Bachelor of Business Management-Master in Business Administration",
        )
        PROFESSIONAL_MBA = "PROFESSIONAL_MBA", "Master in Business Administration"
        PROFESSIONAL_MBA_TOP_EXEC = (
            "PROFESSIONAL_MBA_TOP_EXEC",
            "Master in Business Administration-Top Executive Program",
        )
        PROFESSIONAL_M_GOVERNMENT_MANAGEMENT = (
            "PROFESSIONAL_M_GOVERNMENT_MANAGEMENT",
            "Master in Government Management",
        )
        PROFESSIONAL_M_GOVERNMENT_MANAGEMENT_EXEC = (
            "PROFESSIONAL_M_GOVERNMENT_MANAGEMENT_EXEC",
            "Master in Government Management-Executive Special Program",
        )
        PROFESSIONAL_DBA = "PROFESSIONAL_DBA", "Doctor of Business Administration"
        PROFESSIONAL_DPM = "PROFESSIONAL_DPM", "Doctor of Public Management"
        PROFESSIONAL_MA_SPECIAL_EDUCATION = (
            "PROFESSIONAL_MA_SPECIAL_EDUCATION",
            "Master of Arts in Special Education - Specializing in Development Delays",
        )
        CAUP_BS_ARCH = "CAUP_BS_ARCH", "Bachelor of Science in Architecture (BS Arch)"
        PLM_BS_BSA = "PLM_BS_BSA", "Bachelor of Science in Accountancy (BSA)"
        PLM_BS_BSBA_FM = (
            "PLM_BS_BSBA_FM",
            "Bachelor of Science in Business Administration major in Financial Management (BSBA FM)",
        )
        PLM_BS_BSBA_MM = (
            "PLM_BS_BSBA_MM",
            "Bachelor of Science in Business Administration major in Marketing Management (BSBA MM)",
        )
        PLM_BS_BSBA_OM = (
            "PLM_BS_BSBA_OM",
            "Bachelor of Science in Business Administration major in Operations Management (BSBA OM)",
        )
        PLM_BS_BSBA_HRM = (
            "PLM_BS_BSBA_HRM",
            "Bachelor of Science in Business Administration major in Human Resource Management (BSBA HRM)",
        )
        PLM_BS_BSBA_BE = (
            "PLM_BS_BSBA_BE",
            "Bachelor of Science in Business Administration major in Business Economics (BSBA BE)",
        )
        PLM_BS_BS_ENTRE = (
            "PLM_BS_BS_ENTRE",
            "Bachelor of Science in Entrepreneurship (BS ENTRE)",
        )
        PLM_BS_BSREM = (
            "PLM_BS_BSREM",
            "Bachelor of Science in Real Estate Management (BSREM)",
        )
        PLM_BS_BSHM = (
            "PLM_BS_BSHM",
            "Bachelor of Science in Hospitality Management (BSHM)",
        )
        PLM_BS_BSTM = "PLM_BS_BSTM", "Bachelor of Science in Tourism Management (BSTM)"
        CET_BSCHE = "CET_BSCHE", "Bachelor of Science in Chemical Engineering (BSCHE)"
        CET_BSCE = "CET_BSCE", "Bachelor of Science in Civil Engineering (BSCE)"
        CET_BSCPE = "CET_BSCPE", "Bachelor of Science in Computer Engineering (BSCpE)"
        CET_BSEE = "CET_BSEE", "Bachelor of Science in Electrical Engineering (BSEE)"
        CET_BSECE = (
            "CET_BSECE",
            "Bachelor of Science in Electronics Engineering (BSECE)",
        )
        CET_BSME = "CET_BSME", "Bachelor of Science in Mechanical Engineering (BSME)"
        CET_BSMFGE = (
            "CET_BSMFGE",
            "Bachelor of Science in Manufacturing Engineering (BSMfgE)",
        )
        CISTM_BSCS = "CISTM_BSCS", "Bachelor of Science in Computer Science (BSCS)"
        CISTM_BSIT = (
            "CISTM_BSIT",
            "Bachelor of Science in Information Technology (BSIT)",
        )
        CHASS_BAC = "CHASS_BAC", "Bachelor of Arts in Communication (BAC)"
        CHASS_BSSW = "CHASS_BSSW", "Bachelor of Science in Social Work (BSSW)"
        CHASS_BMMP = "CHASS_BMMP", "Bachelor of Music in Music Performance (BMMP)"
        CN_BSN = "CN_BSN", "Bachelor of Science in Nursing (BSN)"
        CPT_BSPT = "CPT_BSPT", "Bachelor of Science in Physical Therapy (BSPT)"
        CS_BSBIO = "CS_BSBIO", "Bachelor of Science in Biology (BSBio)"
        CS_BSMATH = "CS_BSMATH", "Bachelor of Science in Mathematics (BSMath)"
        CS_BSCHEM = "CS_BSCHEM", "Bachelor of Science in Chemistry (BSChem)"
        CS_BSPSY = "CS_BSPSY", "Bachelor of Science in Psychology (BSPsy)"

    image = models.ImageField(upload_to="profile_images/", null=True, blank=True)
    year_level = models.IntegerField(null=True, blank=True)
    degree = models.CharField(
        choices=Degree.choices, max_length=255, null=True, blank=True
    )

    def get_subscriptions(self, active=None):
        # Fetch user's subscriptions and related items
        if active is not None:
            subscriptions = Subscription.objects.filter(
                user=self, active=active
            ).select_related("item")
        else:
            subscriptions = Subscription.objects.filter(user=self).select_related(
                "item"
            )

        # Sort subscriptions by the item's latest_comment_date field
        subscribed_items = sorted(
            [subscription.item for subscription in subscriptions],
            key=lambda item: item.latest_comment_date or item.created_at,
            reverse=True,
        )

        return subscribed_items

    def subscribe(self, item):
        subscription, created = Subscription.objects.get_or_create(user=self, item=item)
        if not created:
            subscription.active = True
            subscription.save()

    def unsubscribe(self, item):
        subscription = Subscription.objects.get(user=self, item=item)
        if subscription:
            subscription.active = False
            subscription.save()


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
    found_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="found_items",
        null=True,
        blank=True,
    )
    returned_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    latest_comment_date = models.DateTimeField(null=True, blank=True)
    latest_comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Subscribe back to item created by user every time someone comments
        self.user.subscribe(self)


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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update latest_comment of item
        self.item.latest_comment_date = self.created_at
        self.item.latest_comment = self.comment
        self.item.save()
        # Subscribe to item
        self.user.subscribe(self.item)

    def __str__(self):
        length = 100
        return (
            self.comment[:length] + "..."
            if len(self.comment) > length
            else self.comment
        )


class Subscription(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscriptions"
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="subscribers")
    active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "item")

    def __str__(self):
        return f"{self.user.username} subscribed to {self.item.name}"

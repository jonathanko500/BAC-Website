from django.db import models


class SwimLessons(models.Model):
    urgent = models.TextField(blank=True, null=True)
    philosophy = models.TextField(blank=True, null=True)
    registration_info = models.TextField(
        help_text="Separate point by making a new line (hit enter)", blank=True, null=True)
    waitlist_info = models.TextField(
        help_text="Separate point by making a new line (hit enter)", blank=True, null=True)
    policy = models.TextField(
        help_text="Separate point by making a new line (hit enter)", blank=True, null=True)
    display_roadmap = models.BooleanField(
        default=False, help_text="Check this to display the roadmap on the website")
    roadmap_image = models.ImageField(
        upload_to='uploads/lesson/frontPage', blank=True, null=True, help_text="Upload a roadmap image")

    def get_registration_info_as_list(self):
        return self.registration_info.split('\n') if self.registration_info else []

    def get_waitlist_info_as_list(self):
        return self.waitlist_info.split('\n') if self.waitlist_info else []

    def get_policy_info_as_list(self):
        return self.policy.split('\n') if self.policy else []

class lessonInfoHome(models.Model):
    urgent = models.TextField(blank=True, null=True)

    registration_info = models.TextField(blank=True, null=True)

    def get_reg_info_as_list(self):
        return self.registration_info.split('\n') if self.registration_info else []


# Generate choices dynamically for level and max_swimmers
LEVEL_CHOICES = [(i, str(i)) for i in range(1, 6)]  # Levels 1 to 5
MAX_SWIMMERS = [(i, str(i)) for i in range(1, 6)]  # 1 to 5 swimmers


class Group_Lesson_Info(models.Model):
    # Basic information
    name = models.CharField(
        max_length=255, verbose_name="Name of group", blank=True, null=True)
    level = models.IntegerField(
        choices=LEVEL_CHOICES, default=1, verbose_name="Level", blank=True, null=True)
    ages = models.CharField(
        max_length=255, verbose_name="Ages for lessons", blank=True, null=True)
    instructor_swimmer_ratio = models.IntegerField(choices=MAX_SWIMMERS, default=1,
                                                   verbose_name="Instructor/Swimmer ratio", blank=True, null=True)
    description = models.TextField(
        verbose_name="Group Description", blank=True, null=True)
    # Benchmarks and pictures
    benchmark1_name = models.CharField(
        max_length=255, verbose_name="Name of Benchmark 1", blank=True, null=True)
    benchmark1 = models.TextField(
        verbose_name="Benchmark 1 Description", blank=True, null=True)
    picture1 = models.ImageField(upload_to='uploads/lesson/lessonInfo',
                                 verbose_name="Picture for Benchmark 1", blank=True, null=True)

    benchmark2_name = models.CharField(
        max_length=255, verbose_name="Name of Benchmark 2", blank=True, null=True)
    benchmark2 = models.TextField(
        verbose_name="Benchmark 2 Description", blank=True, null=True)
    picture2 = models.ImageField(upload_to='uploads/lesson/lessonInfo',
                                 verbose_name="Picture for Benchmark 2", blank=True, null=True)

    benchmark3_name = models.CharField(
        max_length=255, verbose_name="Name of Benchmark 3", blank=True, null=True)
    benchmark3 = models.TextField(
        verbose_name="Benchmark 3 Description", blank=True, null=True)
    picture3 = models.ImageField(upload_to='uploads/lesson/lessonInfo',
                                 verbose_name="Picture for Benchmark 3", blank=True, null=True)

    benchmark4_name = models.CharField(
        max_length=255, verbose_name="Name of Benchmark 4", blank=True, null=True)
    benchmark4 = models.TextField(
        verbose_name="Benchmark 4 Description", blank=True, null=True)
    picture4 = models.ImageField(upload_to='uploads/lesson/lessonInfo',
                                 verbose_name="Picture for Benchmark 4", blank=True, null=True)

    # Utility methods for benchmarks
    def get_benchmark1_info_as_list(self):
        return self.benchmark1.split('\n') if self.benchmark1 else []

    def get_benchmark2_info_as_list(self):
        return self.benchmark2.split('\n') if self.benchmark2 else []

    def get_benchmark3_info_as_list(self):
        return self.benchmark3.split('\n') if self.benchmark3 else []

    def get_benchmark4_info_as_list(self):
        return self.benchmark4.split('\n') if self.benchmark4 else []

    # String representation of the model
    def __str__(self):
        return self.name if self.name else 'Unnamed Group'


class PrivateSchedule(models.Model):
    urgent = models.TextField(blank=True, null=True)

    lesson1_name = models.CharField(
        max_length=255, blank=True, null=True)
    lesson1_age = models.CharField(
        max_length=255, blank=True, null=True)
    lesson1_description = models.TextField(blank=True, null=True)

    lesson2_name = models.CharField(
        max_length=255, blank=True, null=True)
    lesson2_age = models.CharField(
        max_length=255, blank=True, null=True)
    lesson2_description = models.TextField(blank=True, null=True)

    philosophy_heading = models.CharField(
        max_length=255, blank=True, null=True)
    philosophy_info = models.TextField(blank=True, null=True)

    policy_heading = models.CharField(
        max_length=255, blank=True, null=True)
    policy_info = models.TextField(blank=True, null=True)

    registraion_heading = models.CharField(
        max_length=255, blank=True, null=True)
    registraion_info = models.TextField(blank=True, null=True)

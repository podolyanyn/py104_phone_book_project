from django.db import models


class PhoneNumber(models.Model):
    number = models.CharField(max_length=15)

    def __str__(self):
        return self.number


class Contact(models.Model):
    phone_number = models.OneToOneField(PhoneNumber, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, null=True, blank=True)
    locality = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    social_media = models.CharField(max_length=100, null=True, blank=True)
    black_list_status = models.BooleanField(default=False)

    def __str__(self):
        return f'phone_number: {self.phone_number.number}, name: {self.name}, surname: {self.surname}, ' \
               f'locality: {self.locality}, email: {self.email}, social_media: {self.social_media},' \
               f'black_list_status: {self.black_list_status}'

    def add_to_black_list(self):
        self.black_list_status = True
        self.save()

    def remove_from_black_list(self):
        self.black_list_status = False
        self.save()

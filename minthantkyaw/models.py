from django.db import models


class About(models.Model):
    p_text = models.TextField(max_length=500)
    

class Education(models.Model):
    school=models.CharField(max_length=50)
    degree=models.CharField(max_length=50)
    year=models.CharField(max_length=20)
  

class Skills(models.Model):
    img_link= models.TextField(max_length=500)


class Projects(models.Model):
    prj_img_link=models.TextField(max_length=500)
    prj_title=models.CharField(max_length=50)
    prj_techs=models.CharField(max_length=100)
    prj_github_link=models.TextField(max_length=500)


class Contact(models.Model):
    contact_link=models.CharField(max_length=100)
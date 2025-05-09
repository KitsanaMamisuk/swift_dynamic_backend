from django.db import models


class Gender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    OTHER = 'O', 'Other'
    
    
class Grade(models.TextChoices):
    GRADE_ONE = '1', '1'
    GRADE_TWO = '2', '2'
    GRADE_THREE = '3', '3'
    GRADE_FOUR = '4', '4'
    GRADE_FIVE = '5', '5'
    GRADE_SIX = '6', '6'

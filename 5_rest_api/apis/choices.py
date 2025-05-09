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

class Room(models.TextChoices):
    GRADE_ONE_ROOM_ONE = '1/1', '1/1'
    GRADE_ONE_ROOM_TWO = '1/2', '1/2'
    GRADE_ONE_ROOM_THREE = '1/3', '1/3'
    GRADE_TWO_ROOM_ONE = '2/1', '2/1'
    GRADE_TWO_ROOM_TWO = '2/2', '2/2'
    GRADE_TWO_ROOM_THREE = '2/3', '2/3'
    GRADE_THREE_ROOM_ONE = '3/1', '3/1'
    GRADE_THREE_ROOM_TWO = '3/2', '3/2'
    GRADE_THREE_ROOM_THREE = '3/3', '3/3'
    GRADE_FOUR_ROOM_ONE = '4/1', '4/1'
    GRADE_FOUR_ROOM_TWO = '4/2', '4/2'
    GRADE_FOUR_ROOM_THREE = '4/3', '4/3'
    GRADE_FIVE_ROOM_ONE = '5/1', '5/1'
    GRADE_FIVE_ROOM_TWO = '5/2', '5/2'
    GRADE_FIVE_ROOM_THREE = '5/3', '5/3'
    GRADE_SIX_ROOM_ONE = '6/1', '6/1'
    GRADE_SIX_ROOM_TWO = '6/2', '6/2'
    GRADE_SIX_ROOM_THREE = '6/3', '6/3'
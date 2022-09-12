from django.db import models


class Flyer_Image(models.Model):
    
    # Flyer_image = models.ImageField(upload_to='flyer_imgs/',height_field=None, width_field=None, max_length=200, null = False, blank = False)
    Flyer_image = models.ImageField(upload_to='flyer_imgs/', null = True, blank=True)
    Img_src_url = models.CharField(max_length=500, null=True, blank=True)
    Hash = models.CharField(max_length=200, null=True, blank=True)
    Orientation = models.CharField(max_length=1, null=True, blank=True)
    Flyer = models.ForeignKey('Flyer', on_delete=models.CASCADE, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)


class Flyer(models.Model):
    
    
    boros = [('brooklyn', 'Brooklyn'), ('queens','Queens'), ('manhattan','Manhattan'),
                ('bronx','Bronx'), ('staten','Staten Island'), ('nassau','Nassau')]
    Boro = models.CharField(max_length=10, choices=boros)
    
    Event_date = models.DateField(null=True, blank=True)
    
    Flyer_image = models.ForeignKey(Flyer_Image, on_delete=models.CASCADE, primary_key=True)


    event_types = [('comedy', 'Comedy'), ('food','Food'), ('athletic','Athletic'), ('outdoor','Outdoor'),
                ('sports','Sports'), ('seasonal','Seasonal'), ('rock','Live Music: Rock'), ('drinks','Drinks'),
                ('hipHop','Live Music: HipHop'), ('dance','Live Music: Dance'),
                ('other','Live Music: Other'), ('community', 'Community'),
                ('class', 'Class / Info'),]
    Event_type = models.CharField(max_length=10, choices=event_types)

    Contact_information = models.CharField(max_length=200, default='NONE')
    Address = models.CharField(max_length=200)

    Description = models.CharField(max_length=500,null=True, default='Come by !')
    pub_date = models.DateTimeField(auto_now_add=True)

    Posistion = models.SmallIntegerField(default=0)

    Posted_by_me = models.BooleanField(default=False)

    # def dayOfWeek(this):
    #     return this.Event_date.strftime('%A').lower()

    def isEmail(this):
        if '@' in this.Contact_information:
            return True
        else:
            return False


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class Reminder(models.Model):

    User_email = models.CharField(max_length=200)
    Flyer = models.ForeignKey(Flyer, on_delete=models.CASCADE)

# class Viewer(models.Model):
#     pass

class Event(models.Model):

    Date = models.DateField()
    Day_of_week = models.CharField(max_length=10)
    Flyer = models.ForeignKey(Flyer, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
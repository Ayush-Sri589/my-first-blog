from django.db import models
from django.conf import settings
from django.utils import timezone

# from and import used when we add bits and pieces from other files.
class Post(models.Model):
    # class is a special keyword that means we are defining an object.
    # Post is the name of the special object, our model. It cca have  a different name but start with a capital letter.
    # model.Models se hum indicate karte hain ki isko database mai save karna
    # Now we can define the diferent properties of the model..
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Foreign key indicates a link to another model.
    title = models.CharField(max_length=200) # char field used to define somethong with limited number of characters.
    text = models.TextField() # Textfield for something having unlimited number of characters.
    created_date = models.DateTimeField(default=timezone.now) # Date time field for storing date tim
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        # again you can chnage the name of the method but keep it in lowercase and underscores
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

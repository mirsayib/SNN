from django.db import models
from django.contrib.auth.models import User
from PIL import Image 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = "default_zjgy3n.jpg", upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # Opening the uploaded image
        im = Image.open(self.image)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((300, 300))

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=90)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)

        super(Profile, self).save(*args, **kwargs)



    
    
from django.conf import settings
from django.db import models

class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following_rel', on_delete=models.CASCADE)
    follows = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followers_rel', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'follows')

    def __str__(self):
        return f"{self.follower} follows {self.follows}"

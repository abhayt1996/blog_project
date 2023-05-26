from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    other_details = models.TextField()
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    other_details = models.TextField()
    is_public = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    other_details = models.TextField()
    def __str__(self):
        return f"Like {self.id} for Post {self.post_id} by User {self.user_id}"


from django.db import models

class User(models.Model):
    username=models.TextField()
    def __str__(self):
        return "%s" % self.username

class Sketch(models.Model):
    name=models.TextField()
    description=models.TextField()
    creator=models.ForeignKey(User)
    created=models.DateTimeField(auto_now_add=True)
    lastCompiled=models.DateTimeField(auto_now=True)
    sourceURL=models.TextField(default="")
    def __str__(self):
        return "%s, created by %s on %s" %(self.name, self.creator, self.created)


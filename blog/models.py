from django.db import models

class TaskList(models.Model):
    id = models.AutoField(primary_key=True)
    manage = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None)
    # CASCADE - delete all tasks if user is deleted
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.task + ' | ' + str(self.done)
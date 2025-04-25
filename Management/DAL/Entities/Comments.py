from django.db import models

class Comments(models.Model):
    CommentID = models.AutoField(primary_key=True)
    Content = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)
    
    # Assumes 'Users' is another model defined elsewhere
    UserID = models.ForeignKey(
        'Users',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='comments'
    )
    
    # Assumes 'TaskInformation' is another model defined elsewhere
    TaskID = models.ForeignKey(
        'TaskInformation',
        on_delete=models.CASCADE,
        related_name='comments'
    )

    def __str__(self):
        return f"Comment {self.CommentID} by User {self.UserID} on Task {self.TaskID}"

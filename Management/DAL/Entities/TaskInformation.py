from django.db import models

class TaskInformation(models.Model):
    TaskID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100, null=False)
    Description = models.TextField()
    StartDate = models.DateTimeField(auto_now_add=True)
    DueDate = models.DateField()
    AssignedBy = models.ForeignKey('Users', on_delete=models.CASCADE, related_name='tasks_assigned', default=1)  # default=1
    Status = models.ForeignKey('Status', on_delete=models.CASCADE)
    PriorityID = models.ForeignKey('Priority', on_delete=models.CASCADE)

    def __str__(self):
        return f"Task: {self.Title} (Assigned by: {self.AssignedBy})"
from django.db import models

class TaskData(models.Model):
    AssignedID = models.AutoField(primary_key=True)
    TaskID = models.ForeignKey('TaskInformation', on_delete=models.CASCADE, related_name='task_assignments')
    AssignedTo = models.ForeignKey('Users', related_name='assigned_tasks', on_delete=models.CASCADE)
    PriorityID = models.ForeignKey('Priority', on_delete=models.CASCADE)
    Status = models.ForeignKey('Status', on_delete=models.CASCADE)
    DueDate = models.DateField()

    def __str__(self):
        return f"Task {self.TaskID} assigned to {self.AssignedTo}"

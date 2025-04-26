from django.contrib import admin
from django.contrib import admin
from Management.DAL.Entities.Comments import Comments
from Management.DAL.Entities.Priority import Priority
from Management.DAL.Entities.Status import Status
from Management.DAL.Entities.TaskData import TaskData
from Management.DAL.Entities.TaskInformation import TaskInformation
from Management.DAL.Entities.Users import Users

# Register models in Django Admin

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('UserID', 'UserName', 'firstname', 'lastname')

@admin.register(TaskInformation)
class TaskInformationAdmin(admin.ModelAdmin):
    list_display = ('TaskID', 'Title', 'StartDate', 'DueDate', 'Assignedby', 'Status', 'PriorityID')
    search_fields = ('Title',)

@admin.register(TaskData)
class TaskDataAdmin(admin.ModelAdmin):
    list_display = ('AssignedID', 'TaskID', 'AssignedTo', 'PriorityID', 'Status', 'DueDate')

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('StatusID', 'Status')

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('PriorityID', 'PriorityName')

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('CommentID', 'Content', 'Date', 'UserID', 'TaskID')
    search_fields = ('Content',)




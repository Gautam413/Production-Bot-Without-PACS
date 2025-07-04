
from django import forms
from .assigntasks import TaskAssignment
from django.contrib.auth.models import User

# class TaskAssignForm(forms.ModelForm):
#     assigned_to = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
#     due_minutes = forms.ChoiceField(choices=TaskAssignment._meta.get_field('due_minutes').choices)

#     class Meta:
#         model = TaskAssignment
#         fields = ['assigned_to', 'due_minutes']

from django import forms
from django.contrib.auth.models import User

class TaskAssignForm(forms.Form):
    assigned_to = forms.ModelChoiceField(
        queryset=User.objects.none(),  # set empty initially
        label='Assign To',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    due_minutes = forms.ChoiceField(
        choices=[
            (10, '10 minutes'), (15, '15 minutes'), (30, '30 minutes'),
            (60, '1 hour'), (240, '4 hours'), (1440, '1 day')
        ],
        label='Due In',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamically fetch active technician users each time the form is created
        self.fields['assigned_to'].queryset = User.objects.filter(
            is_staff=True,
            is_superuser=False,
            is_active=True
        )

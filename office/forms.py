from django import forms
# from .models import post,leave

from .models import leave,operation

class operationform(forms.ModelForm):
    class Meta:
        model = operation
        fields = ['firstname','lastname','department','operations']

class leaveform(forms.ModelForm):
    class Meta:
        model = leave
        fields = ['firstname','lastname','department','leavetype','supervisoremail','teamleademail','numberofdays']
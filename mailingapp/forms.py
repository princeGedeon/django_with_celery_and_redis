

from django import forms
from .tasks import send_review_email_task
class ReviewForm(forms.Form):
    name=forms.CharField(
        label="FirstName",min_length=4,max_length=50,widget=forms.TextInput(
            attrs={'class':"form-control mb-3","placeholder":"FirstName","id":"form-firstname"}
        )
    )

    email = forms.EmailField(
        label="email", min_length=4, max_length=200, widget=forms.TextInput(
            attrs={'class': "form-control mb-3", "placeholder": "Email", "id": "form-firstname"}
        )
    )

    review = forms.CharField(
        label="FirstName",  widget=forms.Textarea(
            attrs={'class': "form-control mb-3","rows":'5', "placeholder": "FirstName", "id": "form-firstname"}
        )
    )

    def send_email(self):
        send_review_email_task.delay(self.cleaned_data['name'],self.cleaned_data['email'],self.cleaned_data['review'])


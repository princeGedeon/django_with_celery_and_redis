from django.http import HttpResponse
from django.views.generic.edit import FormView
# Create your views here.
from mailingapp.forms import ReviewForm


class ReviewEmailView(FormView):
    template_name = "review.html"
    form_class = ReviewForm

    def form_valid(self, form):
        form.send_email()
        msg="Merci"
        return  HttpResponse(msg)

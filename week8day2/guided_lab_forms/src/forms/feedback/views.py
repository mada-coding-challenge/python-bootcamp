from django.shortcuts import render, redirect
from .forms import FeedbackForm


def feedback(request):

    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            return redirect("thank_you")

    else:
        form = FeedbackForm()

    return render(request, "feedback.html", {"form": form})


def thank_you(request):
    return render(request, "thank_you.html")
from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)

    email = forms.EmailField()

    message = forms.CharField(
        min_length=20,
        widget=forms.Textarea
    )

    rating = forms.ChoiceField(
        choices=[
            (1, "1"),
            (2, "2"),
            (3, "3"),
            (4, "4"),
            (5, "5"),
        ]
    )
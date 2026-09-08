from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render


def profile(request):
    image_url = None

    if request.method == "POST":
        image = request.FILES.get("image")

        if image:
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            filename = fs.save(image.name, image)
            image_url = fs.url(filename)

    return render(
        request,
    "profile.html",
        {"image_url": image_url},
    )
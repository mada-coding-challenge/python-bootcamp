from django.shortcuts import get_object_or_404, redirect, render
from .models import Post


def feed(request):
    request.session["username"] = "Mada"
    if "username" not in request.session:
        request.session["username"] = "Mada"

    username = request.session["username"]

    posts = Post.objects.all().order_by("-id")

    if request.method == "POST":
        description = request.POST.get("description")
        image = request.FILES.get("image")

        if description and image:
            Post.objects.create(
                username=username,
                description=description,
                image=image,
            )

        return redirect("instagram:feed")

    return render(
        request,
        "index.html",
        {
            "posts": posts,
            "username": username,
        },
    )


def like_post(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, id=post_id)
        post.likes += 1
        post.save()

    return redirect("instagram:feed")
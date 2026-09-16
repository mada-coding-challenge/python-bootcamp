from django.shortcuts import render, redirect


def home(request):
    cart = request.session.get("cart", [])

    theme = request.COOKIES.get("theme", "light")

    return render(request, "home.html", {
        "cart": cart,
        "theme": theme,
    })


def add_product(request, product_id):
    cart = request.session.get("cart", [])

    cart.append(product_id)

    request.session["cart"] = cart

    return redirect("home")


def clear_cart(request):
    request.session.pop("cart", None)

    return redirect("home")


def set_theme(request, theme):
    # Only allow light or dark
    if theme not in ["light", "dark"]:
        theme = "light"

    response = redirect("home")

    # Save theme for 30 days
    response.set_cookie(
        "theme",
        theme,
        max_age=30 * 24 * 60 * 60
    )

    return response
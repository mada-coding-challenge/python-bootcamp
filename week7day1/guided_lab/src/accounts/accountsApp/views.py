from django.views import View
from django.shortcuts import render, redirect


class HomeView(View):

    def get(self, request):
        return render(request, "index.html")


class RegisterView(View):

    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        users = request.session.get("users", {})

        if username in users:
            return render(
                request,
                "register.html",
                {
                    "message": "This username is already registered."
                }
            )

        users[username] = {
            "email": email,
            "password": password,
        }

        request.session["users"] = users

        request.session["username"] = username
        request.session["logged_in"] = True

        return redirect("profile")


class LoginView(View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        users = request.session.get("users", {})

        if username not in users:
            return render(
                request,
                "login.html",
                {
                    "message": "User is not registered."
                }
            )

        if users[username]["password"] != password:
            return render(
                request,
                "login.html",
                {
                    "message": "Invalid username or password."
                }
            )

        request.session["username"] = username
        request.session["logged_in"] = True

        return redirect("profile")


class ProfileView(View):

    def get(self, request):

        if not request.session.get("logged_in"):
            return redirect("login")

        username = request.session.get("username")
        users = request.session.get("users", {})

        user = users.get(username)

        context = {
            "username": username,
            "email": user["email"],
        }

        return render(
            request,
            "profile.html",
            context
        )
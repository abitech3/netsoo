from django.urls import path
from . import views


app_name = "netsooapp"


urlpatterns = [
    path("home", views.home, name="home"),
    path("", views.login_view, name="login"),
    path("forgot", views.forgot, name="forgot"),
    path("signup", views.signup, name="signup"),
    path("profile", views.userProfile, name="profile"),
    path("payment", views.payPlan, name="payment"),
    path("planning", views.postPlan, name="planning"),
    path("viral-post", views.socialPost, name="viral-post"),
    path("faq", views.faq, name="faq"),
    path("contact", views.contactus, name="contact"),
    path("medium", views.medium, name="medium"),
    path("affiliate", views.affilatePlan, name="affiliate"),

]

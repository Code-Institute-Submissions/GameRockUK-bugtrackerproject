from django.conf.urls import url, include
from useraccounts.views import logout, login, registration, user_profile, contact_us
from useraccounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset)),
    url(r'^orderform/', contact_us, name="contactus")
]

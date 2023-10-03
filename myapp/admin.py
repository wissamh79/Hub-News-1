from django.contrib import admin
from .models import User, category, articles, comments, subscriptions, role, choise, poll


# Register your models here.
admin.site.register(User)
admin.site.register(category)
admin.site.register(articles)
admin.site.register(comments)
admin.site.register(subscriptions)
admin.site.register(role)
admin.site.register(choise)
admin.site.register(poll)
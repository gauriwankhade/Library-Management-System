from django.contrib import admin
from .models import Member,Category,Book,Author,IssueRequest

# Register your models here.
admin.site.register(Member)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(IssueRequest)



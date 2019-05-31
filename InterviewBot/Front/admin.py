from django.contrib import admin
from Front.models import UserProfileInfo,questions,result_user,company_post,company_marks
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(questions)
admin.site.register(result_user)
admin.site.register(company_post)
admin.site.register(company_marks)

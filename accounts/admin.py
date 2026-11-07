from django.contrib import admin
from .models import School, Student
#yeh madarchod file jo School aur Django ke built-in Admin Panel ([http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)) par visible, searchable aur filterable banana.
#Agar yeh file empty chhod doge, toh tables database me toh rahengi, lekin Django Admin dashboard par show nahi hongi.
# jush want to show the data base on the website yeh sare help karta hai dekhanae me 

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'user')  # Columns to display in the admin list view
    search_fields = ('name', 'code')  # Searchable fields

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_id', 'school')  # Columns to display in the admin list view
    search_fields = ('student_id', 'email', 'user__username')  # Searchable fields
    list_filter = ('school',)  # Add filter by school

# Optionally, customize how the models are displayed and managed

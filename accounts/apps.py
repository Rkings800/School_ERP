from django.apps import AppConfig
#Iska main kaam hota hai accounts folder ko ek official Django Application ke roop me configure aur introduce karna. 
# Jab bhi Django start hota hai, wo is file ko padhta hai taaki is app ki basic settings aur identity samajh sake

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

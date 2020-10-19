from django.contrib import admin
from .models import User,Product,Category

# Model registration of User Model
admin.site.register(User)

# Model registration of Product Model
admin.site.register(Product)

# Model registration of Category Model
admin.site.register(Category)
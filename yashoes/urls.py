from django.urls import path, include

urlpatterns = [
    path('', include('yashoes.auth.urls')),
    path('products/', include('yashoes.product.urls')),
    path('', include('yashoes.transaction.urls')),
]

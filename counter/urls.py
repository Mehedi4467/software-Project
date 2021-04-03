from django.urls import path
from .import views

urlpatterns = [
    path('Counter/',views.Ticket_counter, name='counter'),
    path('Purchase/',views.Purchase_tricket, name='Purchase'),
    path('Purchase_tricket/<int:id>',views.single_tracket, name='buy'),
    path('pdf_view/<int:id>/',views.pdf_view, name='pdf'),
    
    
]

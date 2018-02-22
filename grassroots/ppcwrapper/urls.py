from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'congressmembers', views.CongressMembersViewSet)
router.register(r'bills', views.RecentBillsViewSet)
router.register(r'positions', views.SpecificVoteSet)
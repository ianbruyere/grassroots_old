from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'congressmembers', views.CongressMembersViewSet)
router.register(r'bills', views.BillsViewSet)
router.register(r'votepositions', views.VotePositionsViewSet)

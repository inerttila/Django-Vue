from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Employee, Review
from .serializers import EmployeeSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

# Create your views here.
class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    @action(detail=True, methods=['patch'])
    def update_thumbs_count(self, request, pk=None):
        print('update_thumbs_count')
        review = self.get_object()
        print('review', review)
        # Assuming your request has thumbsUppCount and thumbsDownCount in the data
        thumbs_up_count = request.data.get('thumbsUppCount')
        thumbs_down_count = request.data.get('thumbsDownCount')

        print('thumbs_up_count', thumbs_up_count)
        print('thumbs_down_count', thumbs_down_count)

        # Perform the update
        review.thumbsUppCount = thumbs_up_count
        review.thumbsDownCount = thumbs_down_count
        review.save()

        serializer = self.get_serializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
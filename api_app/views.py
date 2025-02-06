from django.shortcuts import render, redirect, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_app.models import login_api
from api_app.serializers import loginserializer
import requests

class LoginAPIView(APIView):
    def get(self, request):
        query = login_api.objects.all()
        serializer = loginserializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = loginserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Fixed indentation



def api_data_view(request):
    api_url = "http://127.0.0.1:8000/login/"
    
    if request.method == "POST":
        # Get data from the form (using request.POST)
        Email = request.POST.get("Email")
        password = request.POST.get("password")
        
        # Prepare the data to send in the POST request to your API
        data = {"Email": Email, "password": password}

        # Send POST request to the API
        response = requests.post(api_url, data=data)
        
        if response.status_code == 201:
            # If the POST request is successful, redirect or show a success message
            return redirect('api_data')  # You can also show a success message here
        else:
            # Handle error if API request fails
            error_message = "Error while posting data. Please try again."
            return render(request, 'api_app/login.html', {'error': error_message})

    else:
        # If GET request, fetch and display data
        response = requests.get(api_url)
        api_data = response.json() if response.status_code == 200 else None
        return render(request, 'api_app/login.html', {'api_data': api_data})

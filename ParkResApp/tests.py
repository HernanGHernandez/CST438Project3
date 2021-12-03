from django.test import TestCase, Client

client = Client()
response = client.post(url, content_type='application/json')

# Create your tests here.

from django.http import JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests
import json
import random
import string

class node_detect:
    def __init__(self, node_ulr: str, status: bool):
        self.node_ulr = node_ulr
        self.status = status

    def check_status(self):
        try:
            response = requests.get(self.node_ulr + 'health')
            if response.status_code == 200:
                self.status = True
                return True
            else:
                self.status = False
                return False
        except requests.exceptions.RequestException:
            return False




database = {
    'nodes':[node_detect("http://localhost:8080/", False), node_detect("http://example-node:8080/", False)] 
}

def generate_random_string(length):
    # Генерируем случайную строку из английских букв
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

@csrf_exempt
def process_image_view(request):
    if request.method == 'POST':
        file = request.FILES['file']
        target_url = 'http://localhost:8080/process-image'
        response = requests.post(target_url, files={'file': file})
        
        if response.status_code == 200:
            result = response.json()
            return HttpResponse(json.dumps(result), status=200)
        else:
            return HttpResponse('Error processing the image', status=response.status_code)

@csrf_exempt
def get_active_nodes(request):
    if request.method == 'GET':
        nodes = database['nodes']
        for node in nodes:
            node.check_status()
            
        return HttpResponse(json.dumps([obj.__dict__ for obj in nodes]), status=200)
    else:
        return HttpResponse('Invalid request method', status=405)



@csrf_exempt
def add_server(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if  data['exist'] == 'yes':
            database["nodes"].append(node_detect(data['node_name'], False))
            return HttpResponse( True, status=200)

        
        if  data['exist'] == 'no':
            database["nodes"].append(node_detect(f"https://docker{generate_random_string(10)}.ru:8080/", False))
        else:
            return HttpResponse('Uncorrect Data', status=404)

        return HttpResponse( True, status=200)
    else:
        return HttpResponse('Invalid request method', status=405)


urlpatterns = [
    path('process-image', process_image_view),
    path('get_active_nodes', get_active_nodes),
    path('add_server', add_server),
]
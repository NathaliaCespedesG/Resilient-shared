import os
from django.conf import settings
from django.http import FileResponse, HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import generics
from utils.Withings_ScanWatch.Resilient import Resilient
from typing_extensions import Final
from api.models import Report
from api.serializers import ReportSerializer
import json

@method_decorator(csrf_exempt, name='dispatch')
class WithingsCredentials(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body) # Data tieme status y code 
            # Process the data here
            # For demonstration, we'll just print it and send it back in the response
            code = data['code']
            state = data['state']
            user_id = data['userId']
            username = data['username']
            report = Resilient()
            report.create_credentials(code = code, user_uid = user_id, username = username, role = "study-participant")
            return JsonResponse({'status': 'success', 'data': data})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        
    def get(self, request, *args, **kwargs):
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@method_decorator(csrf_exempt, name='dispatch')
class ReportGeneration(View):

    def get(self, request, *args, **kwargs):
        try:
            #extract data from request args ?
            report_type = request.GET.get('report_type')
            username = request.GET.get('username')
            
            #Answer from Resilient generation
            report_generator = Resilient()
            report = report_generator.report_generation(report_type = report_type, username = username)
            if report['status'] == 'failed':
                return JsonResponse({'status': 'error', 'message': 'Report generation failed'}, status=500)
            
            if report['type'] == 'one':
                file_path = os.path.join('db/General/', report['path'])
                response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename="report.pdf"'
                return response
            
            return JsonResponse({'status': 'success', 'report': report})
        
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)
        
        except ValueError as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

class ReportListCreateView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse({"reports": serializer.data})
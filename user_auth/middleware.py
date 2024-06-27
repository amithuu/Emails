
from Emails import settings # we are accessing this before we check if the debug is true then we showing website url, if false we not are showing url..
from django.utils import timezone
class SimpleMiddleware:
    
    def __init__(self, get_response):
        # if we need any variables we can add here and can use in function below..
        self.get_response = get_response
        self.start_time = None
        self.website ={
            'url':'https:www.google.com',
            'debug':settings.DEBUG,
            'response_time':None,
        }
        
    def __call__(self, request):
        print('running before view is being called')
        response = self.get_response(request)
        return response
    
    
    def process_view(self,request, view_func, view_args, view_kwargs):
        self.start_time = timezone.now() # we are initializing the start_time here because we want the response time of an view, so 
    
    def process_template_response(self, request, response):
        print('this is template response after running view..')
        
        # if settings.DEBUG:# ? if its True, then show the url else not..
        response.context_data['website'] = self.website
        response.context_data['website']['response_time'] = timezone.now() - self.start_time
        
        return response
    
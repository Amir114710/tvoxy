from blog.models import Category
from home.models import *

def config(request):
    call_info = CallInformation.objects.all()
    socialmediaLinks = SocialMediaLinks.objects.all()
    categories = Category.objects.all()
    return {'call_info':call_info , 'socialmediaLinks':socialmediaLinks , 'categories':categories}

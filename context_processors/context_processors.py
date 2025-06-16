from blog.models import Category
from home.models import *
from sell.models import Category as Categories

def config(request):
    call_info = CallInformation.objects.all()
    socialmediaLinks = SocialMediaLinks.objects.all()
    categories = Category.objects.all()
    category = Categories.objects.all()
    return {'call_info':call_info , 'socialmediaLinks':socialmediaLinks , 'categories':categories , 'category':category}

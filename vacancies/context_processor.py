from django.contrib.auth.models import User
def statistics(request):
    return {
        'user': User.objects.filter(username=request.user)
    }
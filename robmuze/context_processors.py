from account.models import Account
from samples.models import Downloads

def user_points(request):
    if request.user.is_authenticated:
        account = request.user.account
        user_points = account.points
    else:
        user_points = None

    return {'user_points': user_points}


def downloadCounter(request):
    if request.user.is_authenticated:
        count = Downloads.objects.filter(user=request.user).count()
        return {'downloadCounter': count }
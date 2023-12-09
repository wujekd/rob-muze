from account.models import Account

def user_points(request):
    if request.user.is_authenticated:
        account = request.user.account
        user_points = account.points
    else:
        user_points = None

    return {'user_points': user_points}

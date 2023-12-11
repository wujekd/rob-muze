from account.models import Account
from samples.models import Downloads
from ankiety.models import AnkietaOtw, OdpowiedzOtw

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
    else:
        count = None
        
    return {'downloadCounter': count }



def unanswered_polls(request):
    if request.user.is_authenticated:
        # Get all polls
        all_polls = AnkietaOtw.objects.all()

        # Check if there are any unanswered polls for the current user
        unanswered_polls_exist = any(
            not OdpowiedzOtw.objects.filter(user=request.user, ankietaotw=poll).exists()
            for poll in all_polls
        )

        # Add the result to the context
        return {'unanswered_polls_exist': unanswered_polls_exist}

    # If the user is not authenticated, default to False
    return {'unanswered_polls_exist': False}

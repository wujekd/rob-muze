from account.models import Account
from samples.models import Downloads
from ankiety.models import AnkietaOtw, OdpowiedzOtw


def user_points(request):
    if request.user.is_authenticated:
        try:
            account = request.user.account
            return {'user_points': account.points}
        except Account.DoesNotExist:
            # If the user doesn't have an account, return 0 points
            return {'user_points': 0}
    else:
        return {'user_points': 0}



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

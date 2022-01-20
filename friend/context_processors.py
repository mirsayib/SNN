from .models import FriendRequest
from collections import Counter

def requests_to_base(requests):
    receivers = dict(Counter([req.receiver for req in FriendRequest.objects.all()]))
    return {'receivers': receivers}
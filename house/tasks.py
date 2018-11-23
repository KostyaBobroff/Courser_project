import requests
from background import app
# from .models import User
from django.contrib.auth import get_user_model
# from house.views import get_user_id
# @app.task
from django.core.cache import cache
def he():
    return 'he'


@app.task
def api():
    users_id = cache.get('ids')
    user = get_user_model()
    for id in users_id:
        # user_id = cache.lpop('ids')
        response = requests.get("http://smarthome.t3st.ru/api/user.controller",
                                headers={'Authorization':
                                             'Bearer {}'.format(user.objects.get(pk=id).api_key)})
        if response.ok:
            data = {elem['name']: elem['value'] for elem in response.json()['data']}
        else:
            data = None
        cache.set("data_{}".format(id), data)
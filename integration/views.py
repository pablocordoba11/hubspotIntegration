from django.http.response import HttpResponse
import requests
from django.http import HttpResponseRedirect
from requests.models import REDIRECT_STATI
from integration.models import *
from django.template import loader
from djangoProject import settings
from django.core import serializers
import datetime


def index(request):
    access_token = ""
    refresh_token = ""
    expire_token = ""
    is_token_valid = False
    token_error = ""

    template = loader.get_template('index.html')
    
    #Here we are validation if the url have a code, that means that the user clicked in authenticate and with that we can 
    # do a call to get the access token to call the api of hubspot

    if 'code' in request.GET and request.GET["code"] != "":
        token_resp = create_token(request.GET["code"])
        if('access_token' in token_resp and token_resp["access_token"] != ""):
            is_token_valid = True
            access_token = token_resp["access_token"]
            refresh_token = token_resp["refresh_token"]
            expire_token = token_resp["refresh_token"]
            #Saving the token in the current user
            username = request.user.get_username()
            user = IntegrationUser.objects.get(user__username=username)
            user.token = access_token
            user.save()
        else:
            is_token_valid =  False
            token_error = token_resp
    context = {
        'latest_question_list': "test",
        'is_token_valid': is_token_valid,
        'invalid_auth': False,
        'access_token': access_token,
        'refresh_token': refresh_token,
        'expire_token': expire_token,
        'token_error': token_error
    }

    return HttpResponse(template.render(context, request))

def create_token(code):
    output = {
        'refresh_token':"",
        'access_token':"",
        'expires_in':"",
        'status':"",
    }
    HUBSPOT_CLIENT_ID = getattr(settings, "HUBSPOT_CLIENT_ID", "")
    HUBSPOT_CLIENT_SECRET = getattr(settings, "HUBSPOT_CLIENT_SECRET", "")
    HUBSPOT_REDIRECT_URL = getattr(settings, "HUBSPOT_REDIRECT_URL", "")

    try:

        data = {
            "grant_type": 'authorization_code',
            "redirect_uri": HUBSPOT_REDIRECT_URL,
            "client_id": HUBSPOT_CLIENT_ID,
            "client_secret": HUBSPOT_CLIENT_SECRET,
            "code": code
        }

        req = requests.post("https://api.hubapi.com/oauth/v1/token", data=data)
        print(req.text)
        if(req.status_code == 200):
            return req.json()
        else:
            raise ValueError("Error Getting the token " + str(req.status_code) + " Detail: " + req.text)
    except Exception as e:
        print("Exception when calling create_token method: %s\n" % e)
        return repr(str(e))

def pull_deals(request, at):
    url = "https://api.hubapi.com/deals/v1/deal/paged?limit=50&properties=dealname&properties=dealstage&properties=closedate&properties=amount&properties=dealtype"
    headers = {"Authorization": "Bearer " + str(at)}

    req = requests.get(url, headers=headers)

    print(req.text)

    if(req.status_code == 200):
        #save the values in the deails
        res = req.json()
        for deal in res.get("deals"):
            obj = {} 
            obj["dealId"] = deal.get("dealId")
            for attr, value in deal.get("properties").items():
                print(attr, '=', value.get("value"))
                if(attr == "closedate"):
                    p_dt = datetime.datetime.fromtimestamp(int(value.get("value"))/1000) 
                    date_formated = p_dt.strftime("%Y-%m-%d") 
                    obj[attr] = date_formated
                else:
                    obj[attr] = value.get("value")
              
            new_deal = Deal(dealId = obj["dealId"], dealname=obj["dealname"], 
                            dealstage=obj["dealstage"], closedate=obj["closedate"],
                            amount=obj["amount"],dealtype=obj["dealtype"])   
            new_deal.save()
        return HttpResponseRedirect("http://localhost:8000/admin/integration/deal/")
    else:
        return (HttpResponse(req.text))



# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import quote  
from urllib.request import urlopen
import redis
import os.path
import json

# Create your views here.

#sadd answers "It is certain" "It is decidedly so" "Without a doubt" "Yes definitely" "You may rely on it" "As I see it, yes" "Most likely" "Outlook good" "Yes" "Signs point to yes" "Reply hazy try again" "Ask again later" "Better not tell you now" "Cannot predict now" "Concentrate and ask again" "Don't count on it" "My reply is no" "My sources say no" "Outlook not so good" "Very doubtful"
r = redis.StrictRedis(host='localhost', port=6379, db = 0);

def fill_db():
    r.set('The Godfather', '{"Authors": "Al Pacino", "Marlon Brando", "Robert Duvall"}', 'Schindlers List', '{"Authors": "Liam Neeson", "Ralph Fennes", "Ben Kingsley"}', 'Saving Private', '{"Authors": "Tom Hanks", "Matt Damon", "Vin Diesel"}')


def show(request):
    f = open('C:/Users/kiosk/Desktop/ExamenWebTech4/movies.txt', 'r');
    file_content = f.read();
    f.close();
    context = {'file_content': file_content};
    return render(request, "test.html", context);


#def results(request, movie):
 	#movielist = {}
    #movie = movie.lower()
    #if (r.get(movie) is None):
        #response = quote(movie)
        #obj = response.read().decode("utf8")
        #movie = json.loads(obj)
        #movie = json.loads(r.get(movie['Authors']))
   # return render(request, 'authors.html', {'authors': authors})



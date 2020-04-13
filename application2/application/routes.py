
from flask import Flask, request, Response
from random import randint 
@app.route('/animal/name', methods=['GET'])
def animal_name():
    animals=[cat,dog,cow]	
    return Response(animals.[randint(0,2)], mimetype='text/plain')

@app.route('/animals/noise', methods=['POST'])
def animal_noise():
    animal=request.data.decode('utf-8')
    if animal=='cat':
       noise='mew'
    elif animal=='dog':
       noise='wof'
    elif animal=='cow':
       noise=='mow'
    else:
       noise='not exist'	
    return Response(noise, mimetype='text/plain')




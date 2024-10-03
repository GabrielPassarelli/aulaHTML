from flask import (Flask, request)
app = Flask(__name__) # cria uma instância

@app.route("/", methods=('GET',)) # Assina uma rota
def index(): 
  nome= request.args.get('nome') #use o seu nome
  #HTML retornado
  return f"""<h1>Página Inicial</h1>
   <p>Olá {nome}, que nome bonito!
   """# função responsável pela página

 # HTML retornado|

@app.route("/outra_pagina", methods =('GET',))
def outra():
  return "<h1>Outra página</h1>"

@app.route("/galeria", methods =('GET',))
def galeria():
  return "<h1>galeria</h1>"

@app.route("/contato", methods =('GET',))
def contato():
  return "<h1>contato</h1>" 

@app.route("/sobre", methods =('GET',))
def sobre():
  return "<h1>sobre</h1>"

def index(): # função responsável pela página
  nome='Rodrigo' #use o seu nome
  #HTML retornado
  return f"""<h1>Página Inicial</h1>
   <p>Olá {nome}, que nome bonito!
   """


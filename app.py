from flask import Flask # Import

app = Flask(__name__) # cria uma instância

@app.route("/", methods=('GET',)) # Assina uma rota
def index(): # função responsável pela página

  return "<h1>Página inicial</h1> <p>Eu sou fulano</p> <hr>" # HTML retornado|

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

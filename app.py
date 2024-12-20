from flask import (Flask, render_template, request)
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

@app.route("/area/<float:largura>/<float:altura>")
def area(largura: float, altura:float):
  return f""" 
<h1> A área informada> L={largura}* A={altura} Area={largura*altura}</h1>"""

@app.route("/par_ou_impar/<float:numero>", methods=('GET',))
def par_ou_impar(numero):
  if numero % 2 == 0:
    return f"O número {numero} é par."
  else:
    return f"O número {numero} é ímpar."
  
@app.route("/sobrenome/<string:nome>/<string:sobrenome>", methods=('GET',))
def nomesobrenome(sobrenome, nome):
  return f"""<h1> sobrenome </h1>
  <p>{sobrenome},{nome}</p>"""

@app.route("/potencia/<float:numero>/<float:elevado>")
def potencia(numero: float, elevado:float):
  return f""" 
<h1> A área informada> n={numero}** e={elevado} Volume={numero**elevado} </h1>"""

@app.route("/tabuada")
@app.route("/tabuada/<num>", methods=("GET", ))
def tabuada(num = None): #None desobriga o valor
  if 'num' in request.args: 
    num = request.args.get('num')
    num = int(request.args.get('num'))     
  return render_template('tabuada.html', num=num)

@app.route("/juros")
@app.route("/juros/<num>", methods=("GET", ))
def juros(juros = None, capital = None, tempo = None, deposito = None): #None desobriga o valor
  if 'juros' and "capital" and "tempo" and "deposito" in request.args: 
    juros = int(request.args.get('juros'))    
    capital = int(request.args.get('juros')) 
    tempo = int(request.args.get('juros')) 
    deposito = int(request.args.get('juros')) 
  return render_template('juros.html', juros=juros, capital=capital, tempo=tempo, deposito=deposito)

@app.route("/login", methods=("GET",))
def login(email=None, senha=None):
  if "email" and "senha" in request.args:
    email = request.args.get("email")
    senha = request.args.get("senha")
  return render_template("login.html", email=email, senha=senha)

@app.route("/imc", methods=("GET",))
def imc(peso = None, altura= None):
  if "peso" and "altura" in request.args:
    peso =float(request.args.get('peso')) 
    altura=float(request.args.get('altura'))
  return render_template("imc.html", peso=peso, altura=altura)
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request,"index.html")
	
def contatos(request):
	if request.method == "GET":
		return render(request, "contatos.html")
	elif request.method == "POST":
		print(request.POST.get('name'))
		print(request.POST.get('email'))
		return render(request,'index.html')
		
def login(request):
	if request.method == "GET":
		print("Acesso via GET")
		return render(request, "login.html")
	elif request.method == "POST":		
		print("Acesso via POST")
		email = request.POST.get("email")
		if request.POST.get("senha") == "teste123":
			print('Usuário {} entrou com sucesso!'.format(email))
			return render(request, "index.html")
		else:
			print('Usuário {} digitou a senha errada'.format(email))
		return render(request, "login.html")

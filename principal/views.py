from django.shortcuts import render,get_object_or_404,redirect
from .models import Reserva, Stand
from .forms import ReservaForm, StandForm

def reserva_editar(request,id):
    reserva = get_object_or_404(Reserva,id=id)
   
    if request.method == 'POST':
        form = ReservaForm(request.POST,instance=reserva)

        if form.is_valid():
            form.save()
            return redirect('reserva_listar')
    else:
        form = ReservaForm(instance=reserva)

    return render(request,'reserva/form.html',{'form':form})


def reserva_remover(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('reserva_listar') # procure um url com o nome 'lista_reserva'


def reserva_criar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST) # formulário preenchido
        if form.is_valid():
            form.save()
            form = ReservaForm()
    else:
    #sempre vem pra cá pela primeira vez, por que o método é GET
        form = ReservaForm()

    return render(request, "reserva/form.html", {'form': form})


def reserva_listar(request):
    reservas = Reserva.objects.all()
    context ={
        'reservas':reservas
    }
    return render(request, "reserva/reserva.html",context)


def index(request):
    total_reservas = Reserva.objects.count()
    total_stands = Stand.objects.count()
    context = {
        'total_reservas' : total_reservas,
        'total_stands' : total_stands,
    }
    return render(request, "reserva/index.html",context)


def stand_editar(request,id):
    stand = get_object_or_404(Stand,id=id)
   
    if request.method == 'POST':
        form = StandForm(request.POST,instance=stand)

        if form.is_valid():
            form.save()
            return redirect('stand_listar')
    else:
        form = StandForm(instance=stand)

    return render(request,"reserva/stand/stands.html",{'form':form})


def stand_remover(request, id):
    stand = get_object_or_404(Stand, id=id)
    stand.delete()
    return redirect('stand_listar') # procure um url com o nome 'lista_stand'


def stand_criar(request):
    if request.method == 'POST':
        form = StandForm(request.POST) # formulário preenchido
        if form.is_valid():
            form.save()
            form = StandForm()
    else:
    #sempre vem pra cá pela primeira vez, por que o método é GET
        form = StandForm()

    return render(request, "reserva/stand/stands.html", {'form': form})


def stand_listar(request):
    stands = Stand.objects.all()
    context ={
        'stands': stands
    }
    return render(request, "reserva/stand/stands.html",context)

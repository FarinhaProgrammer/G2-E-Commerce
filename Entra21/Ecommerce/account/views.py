from django.contrib.auth.decorators import login_required
from account.forms import MyUserForm, EnderecoForm
from django.shortcuts import get_object_or_404, render
from account.models import MyUser

@login_required(login_url='/login/')
def retorna_account(request, pk):
    """
    O retorno consiste em um template acompanhado de um json com as informações do usuário.
    """
    dados = get_object_or_404(MyUser, pk=pk)
    return render(request, 'EM ABERTO', {'dados':dados})


def cadastra_user(request):
    """
    Esta função consiste no cadastro de um novo usuário.
    """
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
        usuario = form.cleaned_data['primeiro_nome']
        return render(request, 'registration/formDoneView.html', {'usuario':usuario})
    else:
        form = MyUserForm()
    return render(request, 'registration/form.html', {'form':form})


@login_required(login_url='/login/')
def addEndereco(request):
    """
    Esta função consiste no cadastro de um novo endereço.
    """
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            endereco = form.save(commit=False)
            endereco.usuario = request.user
            endereco.save()
        return render(request, 'index.html')
    else:
        form = EnderecoForm()
    return render(request, 'registration/addEndereco.html', {'form':form})

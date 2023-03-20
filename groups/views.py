from .models import Apprenant, Brief, Nome
from django.shortcuts import render, redirect
from .forms import ApprenantForm, BriefForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import DeleteView,UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
import random, string

def index(request):
    return render(request, 'groups/index.html')

# def brief_list(request):
    # brief_list = Brief.objects.all()
    # context = {'brief_list': brief_list}
    # return render(request, 'groups/brief_list.html', context)

def apprenant_list(request):
    apprenant_list = Apprenant.objects.all()
    #si methode post avec contenu:
    if request.method == 'POST':
        #on instancie le formulaire avec les données postées
        apprenant_add = ApprenantForm(request.POST)
        #vérifier s'il est valide
        if apprenant_add.is_valid:
            #sauvegarde du fichier
            post = apprenant_add.save()
            post.save()
            return redirect('apprenant_list')
            
    else:
        apprenant_add = ApprenantForm

    context = {'apprenant_list': apprenant_list, 'apprenant_add': apprenant_add}
    return render(request, 'groups/apprenant_list.html', context)

def brief_list(request):
    brief_list = Brief.objects.all()
    #si methode post avec contenu:
    if request.method == 'POST':
        #on instancie le formulaire avec les données postées
        brief_add = BriefForm(request.POST)
        #vérifier s'il est valide
        if brief_add.is_valid:
            #sauvegarde du fichier
            post = brief_add.save()
            post.save()
            return redirect('brief_list')
            
    else:
        brief_add = BriefForm

    context = {'brief_list': brief_list, 'brief_add': brief_add} 
    return render(request, 'groups/brief_list.html', context)

def brief_view(request, brief_id):
    brief = get_object_or_404(Brief, pk = brief_id )
    nome =  Nome.objects.filter(id_brief = brief_id)
    list_final = []
    if nome:
      
        for group in nome:
            list_nome = group.apprenants.values_list()
            list_final.append(list_nome)
            
        if len(list_final[0]) != brief.nb_appr_par_nome:
            context = {'brief': brief}
            Nome.objects.filter(id_brief = brief_id).delete()
            return render(request, 'groups/brief_view.html', context)
        
        else :
            context = {'nome' : nome, 'brief' : brief, 'list_final' : list_final}
            return render(request, 'groups/brief_with_group.html', context)
        
    else :
        # brief = get_object_or_404(Brief, pk = brief_id )
        context = {'brief': brief}
        return render(request, 'groups/brief_view.html', context)



def apprenant_view(request, apprenant_id):
    apprenant = get_object_or_404(Apprenant,pk=apprenant_id)
    #apprenantdel = ApprenantDelete
    context = {'apprenant': apprenant}
    return render(request, 'groups/apprenant_view.html', context)

class ApprenantDelete(DeleteView):
    model = Apprenant
    success_url = reverse_lazy('apprenant')
    template_name = 'apprenant_confirm_delete.html'


def apprenant_del(request, apprenant_id):
    obj = get_object_or_404(Apprenant, id=apprenant_id)
    if request.method=="POST":
      obj.delete()
      return redirect('apprenant_list')
    context = {
        "apprenant" : obj 
    }
    return render(request,'groups/apprenant_confirm_delete.html',context)

def brief_del(request, brief_id):
    obj = get_object_or_404(Brief, id=brief_id)
    if request.method=="POST":
      obj.delete()
      return redirect('brief_list')
    context = {
        "brief" : obj 
    }
    return render(request,'groups/brief_confirm_delete.html',context)


class BriefUpdate(UpdateView):
    model = Brief
    fields = ['titre_brief', 'url_brief', 'nb_appr_par_nome']
    success_url = reverse_lazy('brief_list')
    template_name = 'groups/brief_update.html'

        

    # def get_context_data(self, kwargs):
    #     context = super().get_context_data(kwargs)
    #     return redirect('groups/brief_list.html', context)

class ApprenantUpdate(UpdateView):
    model = Apprenant
    fields = ['nom_apprenant', 'prenom_apprenant']
    success_url = reverse_lazy('apprenant_list')
    template_name = 'groups/apprenant_update.html'




def binomotron(request, brief_id):
    apprenants = list(Apprenant.objects.all())
    obj = get_object_or_404(Brief, id=brief_id)
    nome =  Nome.objects.filter(id_brief = brief_id)
    def creategroupe(groups_lis, nbr_by_groupe):
        liste_appr = []
        liste_nom_bin = []
        newlist = []
        for _ in range(1, len(groups_lis)//nbr_by_groupe):
            nome = random.sample(groups_lis, nbr_by_groupe)
            
            for j in nome:
                groups_lis.remove(j)
            liste_appr.append(nome) 
        liste_appr.append(groups_lis)

        for j in liste_appr:
            str = string.ascii_lowercase
            nom_groupe = ''.join(random.choice(str) for i in range(5))
            liste_nom_bin.append(nom_groupe)
            creat = Nome.objects.create(nome_nom = nom_groupe, id_brief = obj)
            for i in j:
                creat.apprenants.add(i)

        for i,j in zip(liste_appr,liste_nom_bin):
            newlist.append([j,i])
            creat.save()
        return newlist


    if Nome.objects.filter(id_brief = brief_id):
        appr = Nome.objects.all
        context = {'nome' : appr, 'brief' : obj}
        return render(request, 'groups/brief_view.html', context)

    else:    
        a = creategroupe(apprenants, obj.nb_appr_par_nome) 
        context = {'brief' : obj, 'apprenant' : apprenants, 'a' : a}
        return render(request,'groups/binomotron.html',context)
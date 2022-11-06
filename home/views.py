from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Music, SubMusic

style_dict = {
    'techno': 'techno',
    'house': 'house',
    'dnb': 'dnb',
    'nudisco': 'nudisco',
    'electro': 'electro',
    'trance':'trance',
    'ambient':'ambient'
}

def index(request):
    styles_lst = list(style_dict)
    # f"<li><a href='{redirect_path}'><h3>{st.title()}</h3></a></li>"
    context={
        'styles_lst':styles_lst
    }
    return render(request, 'prb/index.html',context)


def get_styles(request, styles:str):
    musics=Music.objects.order_by('-title')
    sub_music=SubMusic.objects.order_by('-style')
    print(sub_music)
    description=style_dict.get(styles)
    styles_lst = list(style_dict)
    data={
        'description_style':description,
        'stl':styles,
        'styles_lst': styles_lst,
        'musics': musics,
        'sub_music': sub_music
    }
    return render(request,'prb/info.html',data)

def get_styles_by_number(request, styles:int):
    styles_lst=list(style_dict)
    if styles>len(styles_lst):
        return HttpResponseNotFound(f'Not found this number style - {styles}')
    name_style=styles_lst[styles-1]
    redirect_url=reverse('electronic-style',args=(name_style,))
    return HttpResponseRedirect(redirect_url)


from django.shortcuts import render

from polls.forms import PlusOneForm, CommentsForm
from .models import Guest, PlusOneGuest, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# TODO: agregar que los campos son requeridos en el +1
# TODO: habilitar cambio de respuestas
# TODO: hacer página inicial
# TODO: habilitar edición de información personal

@login_required(login_url='/polls/login/')
def home(request):
    context = {
        'comments_form' : CommentsForm()
    }
    return render(request, 'polls/home.html', context)


@login_required(login_url='/polls/login/')
def rsvp(request, user_id):
    print("en rsvp")
    guest_object = Guest.objects.get(guest_user=request.user)
    context = {
        'guest': guest_object
    }
    return render(request, 'polls/rsvp.html', context)


@login_required(login_url='/polls/login/')
def send_answer(request, user_id):
    guest_object = Guest.objects.get(guest_user=request.user)
    print("en send_answer")
    try:
        confirm = int(request.POST['choice']) == 1
        guest_object.confirmation_status = confirm
        guest_object.drink_check = request.POST['alcohol']
        guest_object.is_veggie = request.POST['veggie']
        guest_object.save()
    except KeyError:
        # Redisplay the question voting form.
        return rsvp(request, user_id)
    if guest_object.confirmation_status and guest_object.has_plus_one:
        # render plus one question
        return plus_one_form(request, user_id)
    else:
        # render confirmation page
        context = {
            'guest': guest_object
        }
        return render(request, 'polls/show_answer.html', context)


@login_required(login_url='/polls/login/')
def show_answer(request, user_id):
    guest_object = Guest.objects.get(guest_user=request.user)
    print("en show_answer")
    if guest_object.confirmation_status:
        context = {
            'guest': guest_object
        }
        return render(request, 'polls/show_answer.html', context)
    else:
        return rsvp(request, user_id)


@login_required(login_url='/polls/login/')
def plus_one_form(request, user_id):
    guest_object = Guest.objects.get(guest_user=request.user)
    print("(plus_one_form) using user:", request.user)
    print("(plus_one_form) got guest obj:", guest_object)
    form = PlusOneForm()
    context = {
        'has_plus_one': guest_object.has_plus_one,
        'form': form
    }
    return render(request, 'polls/plus_one_info.html', context)


@login_required(login_url='/polls/login/')
def plus_one_info(request, user_id):
    guest_object = Guest.objects.get(guest_user=request.user)
    print("(plus_one_info) using user:", request.user)
    print("(plus_one_info) got guest obj:", guest_object)
    if request.method == "POST":
        form = PlusOneForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            plus_one_object = PlusOneGuest()
            plus_one_object.name = post.name
            plus_one_object.last_name = post.last_name
            plus_one_object.drink_check = post.drink_check
            guest_object.plus_one = plus_one_object
            context = {
                'guest': guest_object
            }
            return render(request, 'polls/show_answer.html', context)
    else:
        return plus_one_form(request, user_id)


@login_required(login_url='/polls/login/')
def make_comment(request):
    print("in make_comment")
    if request.method == "POST":
        print("got post")
        form = CommentsForm(request.POST)
        if form.is_valid():
            print("is valid")
            post = form.save(commit=False)
            this_comment = Comment()
            this_comment.text = post.text
            this_comment.name = request.user.username
            this_comment.save()
            context = {
                'comments_form': CommentsForm(),
                'message': 'Recibimos tu comentario! '
            }
            return render(request, 'polls/home.html', context)
    else:
        return home(request)

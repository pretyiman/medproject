from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView,TemplateView,detail,ListView,UpdateView,DeleteView
from .models import Subject, Topic, Question,PublicMcq,PublicAnswers
from mcq.forms import PublicMcqForm, QuestionForm,AnswerForm,AnswerFormSet
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse_lazy,reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory, formset_factory
from mcq.models import Answers
from django.db import transaction
# Create your views here.

def home_page(request):
    return render (request,'mcq/index.html')

def select_subject(request):
    if request.method == 'GET':
        subjects = Subject.objects.all()
        return render(request, 'mcq/subject_list.html', {'subjects':subjects})

    if request.method == 'POST':
        sublist = request.POST.getlist('subject')
        # print(sublist)
        if sublist == []:
            subjects = Subject.objects.all()
            return render(request, 'mcq/subject_list.html', {'subjects': subjects, 'error':'you selected no ..'})
        subjects = Subject.objects.filter(id__in=sublist)
        return render(request, 'mcq/topic_list.html', {'subjects':subjects})
    
def load_topic(request):
    subject_id = request.GET.get('subject')
    topics = Topic.objects.filter(subject_id=subject_id).order_by('name')
    return render(request, 'mcq/topic_dropdown_list_options.html', {'topics': topics})

def GrandTest(request):
    # if request.method == 'GET':
    if request.method == 'POST':
        topics = request.POST.getlist('topic')
        topics_n_nos = {}
        for t in topics:
            topics_n_nos[t]=request.POST.get(t,'')

        qs = None
        for topic,nos in topics_n_nos.items():
            x = Topic.objects.get(id = topic)
            x = x.question_set.all()[:int(nos)]
            if qs:
                qs.union(x)
            else:
                qs = x
        hidden_q = ''
        print(qs)
        if qs is None:
            return HttpResponseRedirect(reverse('select_subject'))
        for q in qs:
            hidden_q += str(q.id)+'#'
        return render(request, 'mcq/test.html', {'questions':qs, 'hidden_q': hidden_q})


def testresults(request):
    if request.method == 'POST':
        attempted = {}
        hidden_q = request.POST.get("hidden_q", "")
        hidden_q = hidden_q.split('#')
        hidden_q = list(map(int, hidden_q[:-1]))
        for key, value in request.POST.items():
            if key != 'csrfmiddlewaretoken' and key!='hidden_q':
                attempted[key]=value

        q_list = Question.objects.filter(id__in= hidden_q)
        total_correct = 0
        for q, a in attempted.items():
            ques = Question.objects.get(pk = q)
            ans = ques.answers_set.get(pk = a)
            if ans.is_true:
                total_correct +=1

        total_attempted = len(attempted)


        context={'questions':q_list, 'attempted':attempted, 'total_attempted':total_attempted, 'total_correct':total_correct}
        return render(request, 'mcq/testresults.html', context)
    
def test(request, subject, topic, mcq_no):
    # if request.method == "GET":
    s = Subject.objects.get(id=subject)
    t = Topic.objects.get(id=topic)
    selected_questions = Question.objects.filter(subject=s, topic=t)[:mcq_no]
    hidden_q =  ''
    for q in selected_questions:
        hidden_q += str(q.id)+'#'
    return render(request, 'mcq/test1.html', {'questions':selected_questions, 'hidden_q': hidden_q})

    
def single_topic(request):
    if request.method == 'GET':
        subjects = Subject.objects.all()
        topics = Topic.objects.all()
        return render(request, 'mcq/quizetting.html', {'subjects':subjects,'topics':topics})

    if request.method == 'POST':
        subject_id = request.POST.get("subject", "")
        topic_id = request.POST.get("topic", "")
        mcq_no = request.POST.get("mcq_no", "")

        subjects = Subject.objects.all
        if subject_id != '':
            if topic_id != '':
                if int(mcq_no) >= 0 and int(mcq_no) <150:
                    return HttpResponseRedirect(reverse('test', kwargs={'subject':subject_id, 'topic':topic_id, 'mcq_no': mcq_no }))
                else:
                    pass
            else :
                topics = Subject.objects.get(id=subject_id).topic_set.all()
        else:
            topics = Topic.objects.all()
        subject_id = int(subject_id)
        return render(request, 'mcq/quizetting.html', {'subjects':subjects,'topics':topics, 'current_subject_id':subject_id})



def postq(request):
    question = Question()
    # setup a form for the parent
    question_form = QuestionForm(instance=question)


    # AnsewerInlineFormSet = inlineformset_factory(Question, Answers, extra=4)
    AnswerFormSet = inlineformset_factory(
        Question, Answers, form=AnswerForm, extra=4, max_num=4)

    if request.method == "POST":
        question_form = QuestionForm(request.POST)
        formset = AnswerFormSet(request.POST, request.FILES)

        if question_form.is_valid():
            created_question = question_form.save(commit=False)
            formset = AnswerFormSet(
                request.POST, request.FILES, instance=created_question)

            if formset.is_valid():
                created_question.save()
                formset.save()
                return redirect('post_list')
    else:
        author_form = QuestionForm(instance=question)
        formset = AnswerFormSet()

    return render(request, "mcq/testq.html", {
        "question_form": question_form,
        "formset": formset,
    })
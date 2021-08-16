# from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.utils import timezone
# from django.shortcuts import render, get_object_or_404
# from django.urls import reverse
#
# from .models import Question, Choice
#
# # def index_1(request):
# #     # you can create as many db enteries and diplay it from the views
# #     # This is where template comes in
# #     q = Question(question_text="What's new again?", pub_date=timezone.now())
# #     q.save()
# #     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
# #     latest_question_list = Question.objects.order_by('-pub_date')
# #     output = ', '.join([q.question_text for q in latest_question_list])
# #     return HttpResponse(outpu
#
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'poll_app/index.html', context)
#
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404('Question does not exists')
#     return render(request, 'poll_app/index.html', {'question': question})
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id) # from db
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])  # from db also
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'poll_app/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('poll_app:results', args=(question.id,)))
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'poll_app/results.html', {'question': question})



# Amended views:

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone


from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'poll_app/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]
        # refining ..
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'poll_app/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'poll_app/results.html'

def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id) # from db
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])  # from db also
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'poll_app/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll_app:results', args=(question.id,)))


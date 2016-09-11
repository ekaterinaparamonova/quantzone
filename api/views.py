from django.shortcuts import HttpResponse
from django.views.decorators.http import require_POST
from teaching.models import StudentGroupLesson


@require_POST
# Create your views here.
def studentgrouplesson_action(request):
    if request.is_ajax():
        studentgrouplesson_id = request.POST["studentgrouplesson_id"]
        action = request.POST["action"]
        value = request.POST["value"]

        if action == 'visited':
            if value == 'true':
                boolean_value = True
            else:
                boolean_value = False
            studentgrouplesson = StudentGroupLesson.objects.get(pk=studentgrouplesson_id)
            studentgrouplesson.is_visited = boolean_value
            studentgrouplesson.save()
            return HttpResponse('OK')

        if action == 'perm':
            if value == 'true':
                boolean_value = True
            else:
                boolean_value = False
            studentgrouplesson = StudentGroupLesson.objects.get(pk=studentgrouplesson_id)
            studentgrouplesson.has_perm = boolean_value
            studentgrouplesson.save()
            return HttpResponse('OK')

        if action == 'own':
            studentgrouplesson = StudentGroupLesson.objects.get(pk=studentgrouplesson_id)
            studentgrouplesson.own_score = int(value)
            studentgrouplesson.save()
            return HttpResponse('OK')

        if action == 'score':
            studentgrouplesson = StudentGroupLesson.objects.get(pk=studentgrouplesson_id)
            studentgrouplesson.teacher_score = int(value)
            studentgrouplesson.save()
            return HttpResponse('OK')

    return HttpResponse('не OK')
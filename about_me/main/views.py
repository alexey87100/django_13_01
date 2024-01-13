from django.shortcuts import render, redirect
from django.http import Http404

from .data import EMPLOYEES, SKILLS


def index(request):
    """Главная страница."""
    context = {
        'employees': EMPLOYEES
    }
    return render(request, 'index.html', context)


EMPLOYEES_DICT = {employee['id']: employee for employee in EMPLOYEES}

SKILLS_ID = {skill['id']: skill for skill in SKILLS}


def detail(request, employee_id):

    if employee_id in EMPLOYEES_DICT.keys():
        employee = EMPLOYEES_DICT[employee_id].copy()
        list_skills = []
        for skill_id in employee['skills']:
            for elem in SKILLS:
                if skill_id == elem['id']:
                    list_skills.append(elem['name'])
                    break
        employee['skills'] = list_skills
        context = {
            'employee': employee
        }
        return render(request, 'detail.html', context)
    raise Http404("Нет такого сотрудника")
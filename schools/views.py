from django.shortcuts import render
from .models import School, Student, Result

def check_result(request, school_code=None):
    school = None
    results = None
    student = None
    error = None
    total_score = 0
    average = 0
    remark = ""

    if school_code:
        try:
            school = School.objects.get(code__iexact=school_code)
        except School.DoesNotExist:
            error = "School Code not found!"
            return render(request, 'schools/check_result.html', {'error': error})

    if request.method == 'POST':
        pin = request.POST.get('pin', '').strip()
        if school:
            try:
                student = Student.objects.get(pin=pin, school=school)
                results = Result.objects.filter(student=student)
                if results.exists():
                    total_score = sum([r.score for r in results])
                    average = round(total_score / results.count(), 2)
                    if average >= 70:
                        remark = "Excellent - Distinction"
                    elif average >= 60:
                        remark = "Very Good"
                    elif average >= 50:
                        remark = "Good"
                    else:
                        remark = "Needs Improvement"
                else:
                    error = "No result found for this PIN yet - add result in admin!"
            except Student.DoesNotExist:
                error = f"Invalid PIN {pin} for {school.name}!"

    return render(request, 'schools/check_result.html', {
        'school': school,
        'student': student,
        'results': results,
        'error': error,
        'total_score': total_score,
        'average': average,
        'remark': remark,
    })
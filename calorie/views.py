from django.shortcuts import render

def calculator(request):

    calories = {
        "가볍게 걷기": 180,
        "빠르게 걷기": 300,
        "요가": 150,
        "볼링": 198,
        "스트레칭 체조": 174,
        "자전거타기": 264,
        "등산": 300,
        "춤추기": 288,
        "승마": 346,
        "탁구": 360,
        "테니스": 432,
        "배드민턴": 346,
        "배구": 420,
        "축구": 540,
        "농구": 558,
        "스키": 492,
        "에어로빅": 354,
        "팔굽혀펴기": 252,
        "계단 오르내리기": 348,
        "윗몸 일으키기": 606,
        "핸드볼": 600,
        "줄넘기": 624,
        "격렬한 달리기": 630,
        "수영": 720,
    }

    result = None
    exercise = ""
    minutes = ""
    intensity = ""

    if request.method == "POST":

        exercise = request.POST.get("exercise")
        minutes = float(request.POST.get("minutes"))
        intensity = request.POST.get("intensity")

        intensity_rate = {
            "낮음": 0.8,
            "중간": 1.0,
            "높음": 1.2
        }

        base_calorie = calories[exercise]

        result = (
            base_calorie
            * (minutes / 60)
            * intensity_rate[intensity]
        )

    context = {
        "exercises": calories.keys(),
        "result": result,
        "exercise": exercise,
        "minutes": minutes,
        "intensity": intensity,
    }

    return render(
        request,
        "calorie/calculator.html",
        context
    )
from django.http import HttpResponse
from django.shortcuts import render


def title(request):
    return render(request,"index.html")

def About(request):
    read = request.GET.get("text", "Default")
    remove = request.GET.get("Remove", "OFF")
    capital = request.GET.get('AllCapital', 'OFF')
    remover = request.GET.get("Remover", "OFF")
    space_remover = request.GET.get("SpaceRemove", "OFF")  # New line to get the space remover option
    char_count = request.GET.get("CharCount","OFF")

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    if remove == "on":
        Analze = ""
        for char in read:
            if char not in punctuations:
                Analze += char

        value = {"Purpose": "RemoveDone", "analzed_text": Analze}
        return render(request, "Analze.html", value)

    elif capital == 'on':
        Analze = ''
        for char in read:
            Analze += char.upper()
        value = {"Purpose": "All Capital", "analzed_text": Analze}
        return render(request, "Analze.html", value)


    elif remover == 'on':
        Analze = ''
        for char in read:
            if char != "\n" and char !="\r":
                Analze += char
        value = {"Purpose": "Line Remover", "analzed_text": Analze}
        return render(request, "Analze.html", value)


    elif space_remover == 'on':
        Analze = ''
        for char in read:
            if char != " ":
                Analze += char
        value = {"Purpose": "Space Remover", "analzed_text": Analze}
        return render(request, "Analze.html", value)


    elif char_count == 'on':
        count=f"No of Character Count is : {len(read)}"
        value={"Purpose":"CharCounter","analzed_text": count }
        return render(request, "Analze.html", value)



    else:
        value = {"Purpose": "Remove Not Done", "analzed_text": read}
        return render(request, "Analze.html", value)


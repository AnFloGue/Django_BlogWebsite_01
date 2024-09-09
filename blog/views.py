from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse
from django.http import HttpResponse

posts = [
    {
        "id": 1,
        "title": "Let's explore python",
        "description": (
            "Python is an interpreted, high-level, general-purpose programming language. "
            "Widely used in the fields of web development, data science, and machine learning."
        )
    },
    {
        "id": 2,
        "title": "Let's explore Javascript",
        "description": (
            "Javascript is an interpreted, high-level, general-purpose programming language. "
            "Widely used in the fields of web development."
        )
    },
    {
        "id": 3,
        "title": "Django the best web framework",
        "description": (
            "Django is used by almost every big tech company like Facebook, Google, YouTube, Instagram, etc."
        )
    }
]
# posts = [   ]
def home(request):
    context = {"posts": posts}  # Correct the dictionary key
    return render(request, 'home.html', context)



def post(request):
    

    return render(request, 'post.html')

def post_by_id(request, id):
    selected_post = None
    for post in posts:
        if post['id'] == id:
            selected_post = post
            break
    if selected_post is None:
        return HttpResponse("Post not found", status=404)
    
    html = f"""
    <div>
        <h1>ID: {selected_post['id']}</h1>
        <h1>title: {selected_post['title']}</h1>
        <p>{selected_post['description']}</p>
    </div>
    """
    return HttpResponse(html)

def google(request, id):
    return HttpResponseRedirect(f"/post/{id}")
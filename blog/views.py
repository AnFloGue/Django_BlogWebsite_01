from django.shortcuts import render
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
def home(request):
    html = ""
    for post in posts:
        html += f"""
        <div>
            <h1>ID: {post['id']}</h1>
            <h1>title: {post['title']}</h1>
            <p>{post['content']}</p>
        </div>
        """
        print(html)
        print("----------------------------------------")
    return HttpResponse(html)

def post(request, id):
    id = int(id)
    selected_post = None
    print(request)
    
    for post in posts:
        print(post)
        if post['id'] == id:
            selected_post = post
            print(selected_post)
            break
            
    if selected_post is None:
        return HttpResponse("Post not found", status=404)
    
    return HttpResponse(selected_post['description'])
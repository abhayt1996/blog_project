from django.http import JsonResponse, HttpResponseNotFound, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from .models import User, Post, Like

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        other_details = request.POST.get('otherDetails')

        # Perform necessary validation

        user = User(name=name, email=email, password=password, other_details=other_details)
        user.save()

        return JsonResponse({'id': user.id}, status=201)

    return HttpResponseNotFound()

def get_user(request, id):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=id)
            return JsonResponse({'id': user.id, 'name': user.name, 'email': user.email, 'otherDetails': user.other_details})
        except User.DoesNotExist:
            return HttpResponseNotFound()

    return HttpResponseNotFound()

@csrf_exempt
def update_user(request, id):
    if request.method == 'PUT':
        try:
            user = User.objects.get(id=id)

            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            other_details = request.POST.get('otherDetails')

            # Perform necessary validation

            user.name = name
            user.email = email
            user.password = password
            user.other_details = other_details
            user.save()

            return JsonResponse({'id': user.id}, status=200)
        except User.DoesNotExist:
            return HttpResponseNotFound()

    return HttpResponseNotFound()

def delete_user(request, id):
    if request.method == 'DELETE':
        try:
            user = User.objects.get(id=id)
            user.delete()
            return JsonResponse({}, status=200)
        except User.DoesNotExist:
            return HttpResponseNotFound()

    return HttpResponseNotFound()

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        content = request.POST.get('content')
        other_details = request.POST.get('otherDetails')

        # Perform necessary validation

        post = Post(title=title, description=description, content=content, other_details=other_details)
        post.save()

        return JsonResponse({'id': post.id}, status=201)

    return HttpResponseNotFound()

def get_post(request, id):
    if request.method == 'GET':
        try:
            post = Post.objects.get(id=id)

            # Assuming user ID is provided as a query parameter
            user_id = request.GET.get('user_id')

            if post.is_public or post.user_id == user_id:
                return JsonResponse({'id': post.id, 'title': post.title, 'description': post.description, 'content': post.content, 'otherDetails': post.other_details})
            else:
                return HttpResponseForbidden()

        except Post.DoesNotExist:
            return HttpResponseNotFound()

    return HttpResponseNotFound()

@csrf_exempt
def update_post(request, id):
    if request.method == 'PUT':
        try:
            post = Post.objects.get(id=id)

            # Assuming user ID is provided in the request body
            user_id = request.POST.get('user_id')
            title = request.POST.get('title')
            description = request.POST.get('description')
            content = request.POST.get('content')
            other_details = request.POST.get('otherDetails')

            # Check post ownership
            if post.user_id == user_id:
                post.title = title
                post.description = description
                post.content = content
                post.other_details = other_details
                post.save()

                return JsonResponse({'id': post.id}, status=200)
            else:
                return HttpResponseForbidden()

        except Post.DoesNotExist:
            return HttpResponseNotFound()

    return HttpResponseNotFound()

def delete_post(request, id):
    if request.method == 'DELETE':
        try:
            post = Post.objects.get(id=id)
            post.delete()
            return JsonResponse({}, status=200)
        except Post.DoesNotExist:
            return HttpResponseNotFound()

    return HttpResponseNotFound()

@csrf_exempt
def create_like(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        post_id = request.POST.get('post_id')

        # Perform necessary validation

        like = Like(user_id=user_id, post_id=post_id)
        like.save()

        return JsonResponse({'id': like.id}, status=201)

    return HttpResponseNotFound()

def get_like(request, id):
    if request.method == 'GET':
        try:
            like = Like.objects.get(id=id)
            return JsonResponse({'id': like.id, 'user_id': like.user_id, 'post_id': like.post_id})
        except Like.DoesNotExist:
            return HttpResponseNotFound()

    return HttpResponseNotFound()

@csrf_exempt
def update_like(request, id):
    if request.method == 'PUT':
        try:
            like = Like.objects.get(id=id)
            user_id = request.POST.get('user_id')
            post_id = request.POST.get('post_id')

            # Perform necessary validation

            like.user_id = user_id
            like.post_id = post_id
            like.save()

            return JsonResponse({'id': like.id}, status=200)
        except Like.DoesNotExist:
            return HttpResponseNotFound()

    return HttpResponseNotFound()

def delete_like(request, id):
    if request.method == 'DELETE':
        try:
            like = Like.objects.get(id=id)
            like.delete()
            return JsonResponse({}, status=200)
        except Like.DoesNotExist:
            return HttpResponseNotFound()

    return HttpResponseNotFound()

from .models import Post

def add_variable_to_context(request):
    return {
        'lastPost': Post.objects.order_by('-date_posted')[0]
    }
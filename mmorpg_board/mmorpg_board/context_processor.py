from users.forms import AuthenticationForm

def get_context(request):
    context = {
        'login': AuthenticationForm()
    }
    return context
def add_variable_to_context(request):
    return {
        'testme': request.user_id
    }

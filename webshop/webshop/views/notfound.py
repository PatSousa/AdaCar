from pyramid.view import notfound_view_config


@notfound_view_config(renderer='json')
def notfound_view(request):
    request.response.status = 404
    return {'response': 'HTTP 404 - not found'}

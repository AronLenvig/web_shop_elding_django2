def breadcrumb_processor(request):
    path = request.path.split('/')
    breadcrumbs = []
    for i, segment in enumerate(path):
        if segment:
            breadcrumbs.append({'name': segment.title(), 'url': '/'.join(path[:i + 1])})
    print(breadcrumbs)
    return {'breadcrumbs': breadcrumbs}
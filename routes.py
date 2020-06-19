from views import index, get_users


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_post('/get_users', get_users)
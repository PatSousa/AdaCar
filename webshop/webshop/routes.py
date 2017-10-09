def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('products_collections', '/') # verbs allowed: GET
    config.add_route('orders_collections', '/order') # verbs allowed: GET, POST
    config.add_route('orders', '/order/{order_id}') # verbs allowes: GET, POST, PUT, DELETE

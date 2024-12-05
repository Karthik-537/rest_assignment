path_method_dict = {
    "person/create/": {
        "POST": "create_person"
    }
}


def person_create_(request, *args, **kwargs):
    from dsu.dsu_gen.openapi.utils.get_operations_dict import get_operations_dict
    operations_dict = get_operations_dict(path_method_dict, request.path)

    from dsu.dsu_gen.openapi.wrappers.router_wrapper import router_wrapper
    response = router_wrapper("test_app", "person_create_", operations_dict, request, *args, **kwargs)
    return response
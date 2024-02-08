""" 1)This is equivalent to PHP code in Python """

# class SomeObject:
#     def __init__(self, name):
#         self.name = name

#     def get_object_name(self):
#         return self.name


# class SomeObjectsHandler:
#     def __init__(self):
#         pass

#     def handle_objects(self, objects):
#         handlers = []
#         for obj in objects:
#             if obj.get_object_name() == "object_1":
#                 handlers.append("handle_object_1")
#             if obj.get_object_name() == "object_2":
#                 handlers.append("handle_object_2")
#         return handlers


# objects = [SomeObject("object_1"), SomeObject("object_2")]

# soh = SomeObjectsHandler()

# print(soh.handle_objects(objects))

""" Solution 1 """


class SomeObject:
    def __init__(self, name):
        self.name = name

    def get_object_name(self):
        return self.name


class SomeObjectsHandler:
    def __init__(self):
        self.handlers = {}

    def register_handler(self, object_name, handler):
        self.handlers[object_name] = handler

    def handle_objects(self, objects):
        handlers = []
        for obj in objects:
            object_name = obj.get_object_name()
            if object_name in self.handlers:
                handlers.append(self.handlers[object_name])
        return handlers


def handle_object_1(obj):
    return "handle_object_1"


def handle_object_2(obj):
    return "handle_object_2"


objects = [SomeObject("object_1"), SomeObject("object_2")]

soh = SomeObjectsHandler()
soh.register_handler("object_1", handle_object_1)
soh.register_handler("object_2", handle_object_2)

print(soh.handle_objects(objects))


""" 2)This is equivalent to PHP code in Python """

# class XMLHttpService:
#     pass

# class Http:
#     def __init__(self, xml_http_service: XMLHttpService):
#         self.service = xml_http_service

#     def get(self, url: str, options: list):
#         self.service.request(url, 'GET', options)

#     def post(self, url: str):
#         self.service.request(url, 'POST')

""" Solution 2 """


class XMLHttpService:
    def request(self, url, method, options):
        # Implementing an HTTP request using XMLHttpService
        pass


class HttpServiceInterface:
    def request(self, url, method, options):
        pass


class Http:
    def __init__(self, http_service: HttpServiceInterface):
        self.service = http_service

    def get(self, url, options):
        self.service.request(url, "GET", options)

    def post(self, url):
        self.service.request(url, "POST")

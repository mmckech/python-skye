class MyClass:
    """A simple example class"""
    DEFAULT_GREETING = "hello world"

    def __init__(self, thegreeting = DEFAULT_GREETING):
        self.greeting = thegreeting

    def greet(self, name = None):
        response = self.greeting
        if name:
            response += ", " + name
        return response

class Page:
    # This is the method each subclass must implement to render the page.
    def render(self):
        raise NotImplementedError("Subclasses must implement the render method")

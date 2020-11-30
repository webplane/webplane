
class WebTemplateHandler:
    """ Render templates from a webroot dir """

    def __init__(self, path, template_engine, render_func=None):
        self._path = path
        self._template_engine = template_engine
        self._render_func = render_func
        self._name = path

    @controller.publish
    def index(self):
        kwargs = {}
        if self._render_func:
            kwargs = self._render_func()
        return self._template_engine.render(self._path, controller.get_lang(), **kwargs)

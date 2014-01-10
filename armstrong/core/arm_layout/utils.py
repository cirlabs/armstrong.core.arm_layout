import warnings
from armstrong.utils.backends import GenericBackend

render_model = (GenericBackend("ARMSTRONG_RENDER_MODEL_BACKEND",
        defaults="armstrong.core.arm_layout.backends.BasicRenderModelBackend")
    .get_backend())


# DEPRECATED: To be removed in ArmLayout 1.4. Here for backwards compatibility
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

def deprecate(func):
    def wrapper(*args, **kwargs):
        msg = "Importing `{}` from this module is deprecated and will be removed in ArmLayout 1.4"
        warnings.warn(msg.format(func.__name__), DeprecationWarning)
        return func(*args, **kwargs)
    return wrapper

mark_safe = deprecate(mark_safe)
render_to_string = deprecate(render_to_string)
get_layout_template_name = deprecate(render_model.get_layout_template_name)

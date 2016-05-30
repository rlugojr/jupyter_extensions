imports = ['base/js/namespace', 'require']

themes = ['default', 'oceans16', 'grade3', 'space-legos']

def load(Jupyter, require):
    from .utils import load_css, unload_css, get_metadata, set_metadata
    load_css('./style.css')

    def main():
        def on_theme_changed():
            theme = select.val()
            unload_css(themes[1:])
            if theme != 'default':
                load_css('./themes/%s.css' % theme)
            set_metadata(Jupyter.notebook, 'theme', theme)
                
        select = jQuery('<select/>').attr('id', 'scpy3-theme-selector')
        select.addClass('form-control select-xs')
        select.append(jQuery('<optgroup label = "Themes:">'))
        for theme in themes:
            select.append(jQuery('<option/>').attr('value', theme).text(theme))
        select.change(on_theme_changed)
        Jupyter.toolbar.element.append(select)

        theme = get_metadata(Jupyter.notebook, 'theme')
        if theme is not None:
            select.val(theme)
            on_theme_changed()
    
    return {"load_ipython_extension": main}

define(imports, load)
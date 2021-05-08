from simple_structure import app
# from .complex_structure import app


if __name__ == '__main__':
    print(app.view_functions)
    print(app.url_map)
    app.run()

from utm import create_app

app = create_app()


for route in app.routes:
    print(route)
print(app.docs_url)

from utm import create_app

app = create_app()

for rt in app.routes:
    print(rt)

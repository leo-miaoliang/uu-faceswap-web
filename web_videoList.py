from web import create_app

app = create_app()
app.secret_key = '12344d'

if __name__ == "__main__":
    app.run()

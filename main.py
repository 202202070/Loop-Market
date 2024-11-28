from __init_py__ import create_app

app=create_app()

if __name__ == '__main__':
    app.run(debug=True)
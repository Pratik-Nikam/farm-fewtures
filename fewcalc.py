from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) 

@app.shell_context_processor
def make_shell_context():
    return {}
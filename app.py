from web import CreateApp

if __name__ == '__main__':

    app = CreateApp()
    app.run(debug=True, host='0.0.0.0')

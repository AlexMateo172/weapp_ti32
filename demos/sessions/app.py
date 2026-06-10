import web

# DEBUG ACTIVADO para ver el error real
web.config.debug = False

urls = (
    '/', 'Index',
    '/count', 'Count',
    '/reset', 'Reset'
)

app = web.application(urls, locals())

# Sesiones
if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'count': 0})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()

class Count:
    def GET(self):
        session.count += 1
        return render.count(count=session.count)

class Reset:
    def GET(self):
        session.kill()
        return render.reset()

if __name__ == "__main__":
    app.run()
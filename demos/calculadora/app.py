import web
import math #Importa fucniones matematicas como la raiz o la potencia 

urls = (
    '/', 'Index',
    '/calculadora','Calculadora'
)
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()
    
class Calculadora:
    def GET(self):
        numero_1=0.0
        numero_2=0.0
        resultado=0.0
        return render.calculadora(numero_1, numero_2, resultado)
    
    
    def POST(self):
        formulario = web.input()
                                                         # Uso .get() con 0.0 como valor predeterminado si el campo está vacío
        numero_1 = float(formulario.get('prinum', 0.0))
        numero_2 = float(formulario.get('segnum', 0.0))
        operacion = formulario.get('operacion', '')
        
        resultado = 0.0


        if  operacion == "sumar":
            resultado = numero_1 + numero_2
        
        if  operacion == "restar":
            resultado = numero_1 - numero_2

        if  operacion == "multiplicar":
            resultado = numero_1 * numero_2

        if  operacion == "dividir":
            resultado = numero_1 / numero_2

        if operacion == "raiz":
            resultado = math.sqrt(numero_1)

        if operacion == "potencia":
            resultado = math.pow(numero_1, numero_2) #El pow se usa para calcular la potencia de un numero 

        if operacion == "modulo":
            resultado = numero_1 % numero_2

        if operacion == "limpiar":
            numero_1 = 0.0
            numero_2 = 0.0
            resultado = 0.0                


        return render.calculadora(numero_1, numero_2, resultado)

if __name__ == "__main__":
    app.run()
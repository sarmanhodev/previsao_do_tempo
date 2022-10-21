from flask import Flask, render_template,request
import requests



app = Flask(__name__, template_folder='./template')
API_KEY = "CHAVE DE ACESSO" #NECESSÁRIO CADASTRAR-SE PARA TER SUA CHAVE DE ACESSO

@app.route("/previsao", methods=["GET", "POST"])
def previsao():
    #search=str(input("\nBusca por cidade ou país =>  "))
    
    search = request.form.get('cidade')
    url=f"https://api.openweathermap.org/data/2.5/weather?q={search}&appid={API_KEY}&lang=pt_br"

    requisicao = requests.get(url)
    requisicao_dic = requisicao.json()
    descricao = requisicao_dic['weather'][0]['description']
    temperatura = requisicao_dic['main']['temp'] - 273.15
    veloc_vento = requisicao_dic['wind']['speed']
    icone = requisicao_dic['weather'][0]['icon']
    temperatura_minima = requisicao_dic['main']['temp_min'] - 273.15
    temperatura_maxima = requisicao_dic['main']['temp_max'] - 273.15
    umidade = requisicao_dic['main']['humidity']
    print("\nLocalidade: "+str(search))
    print(descricao, f"{round(temperatura,1)}ºC")
    print("TEMPERATURA MÁXIMA "+str(temperatura_maxima))
        
    #print("\nA temperatura para {} é de {} \n".format(search,temperatura))
    #return redirect(url_for('inicial'))
        
    

    return render_template("home.html", descricao = descricao,
    icone = icone,
    veloc_vento = veloc_vento,
     temperatura=round(temperatura,1),
     temperatura_minima = round(temperatura_minima,2),
     temperatura_maxima = round(temperatura_maxima,2), 
     umidade = umidade,
     localidade=search)


if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')
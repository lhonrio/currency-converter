<h1 align='center'>
    Conversor de Moedas
</h1>

<h2>Objetivo do Projeto:</h2>
Ao realizar uma requisição <b>(GET)</b> com o valor em reais que você quer converter, deve-se obter como resultado o valor convertido nas 3 principais moedas do mundo (<b>USD, EUR e GBP</b>) com a cotação em tempo real. 
<br>
<br>
<h2>Tecnologias Utilizadas:</h2>

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas)
- Bibliotecas: Requirements.txt

<h2>Exemplo:</h2>

- <b>Input:</b> Valor em Reais

```json
{
    "value": 11
}
````

- <b>Output:</b> Retorno em 3 diferentes moedas (USD, EUR e GBP)
</br>

```json
{
    "USD": 2.3,
    "EUR": 1.83,
    "GBP": 1.52
}
````
<h2>Clone o Repositório:</h2>

````bash
$ git clone https://github.com/lhonrio/currency-converter.git
````
<h3><b>OBS:</h3></b> Após rodar a aplicação a mesma será iniciada na porta 5000. </br>
</br>Para conferir o funcionamento da API utilize o Postman ou um aplicativo de sua preferencia com a seguinte URL: https://127.0.0.1:5000/converter
</br>
</br>Para consultar a documentação da API consulte: https://127.0.0.1:5000/docs 
</br>
</br><h3><b>Desenvolvido por:</h3></b>

- [Lucas Honório Lima](https://www.linkedin.com/in/lhonrio/)
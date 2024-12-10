import requests
import ANSI as A

def get_exchange_rate(from_currency, to_currency):
    api_key = "fea2ba5a66eddc48906104feab5a063e"
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        rate = data["rates"][to_currency]
        return rate
    except requests.exceptions.RequestException as e:
        print("Erro ao acessar a API:", e)
        return None
    except KeyError:
        print("Moeda inválida ou erro na resposta da API.")
        return None

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate:
        converted_amount = amount * rate
        return converted_amount
    else:
        return None

def main():
    print(f"""
          {A.SUBLINHADO}{A.NEGRITO}=== CONVERSOR DE MOEDAS ==={A.RESET}
            """)
    from_currency = input("Digite a moeda de origem (ex: BRL): ").upper()
    to_currency = input("Digite a moeda de destino (ex: USD): ").upper()
    amount = float(input("Digite o valor a ser convertido: "))

    converted_amount = convert_currency(amount, from_currency, to_currency)
    if converted_amount is not None:
        print(f"{amount} {from_currency} equivale a {converted_amount:.2f} {to_currency}")
    else:
        print("Não foi possível realizar a conversão.")

if __name__ == "__main__":
    main()

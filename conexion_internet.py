import requests

print("--- POKEDEX EN PYTHON ---")
pokemon = input("Escribe el nombre de un Pokemon: ").lower()

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
respuesta = requests.get(url)

if respuesta.status_code == 200:
    datos = respuesta.json()

    print(f"\n¡Pokemon encontrado! [{datos['name'].capitalize()}]")
    print(f"- Altura: {datos['height']} decímetros")
    print(f"- Peso: {datos['weight']} hectogramos")
else:
    print("\n [!] Error: Ese Pokemon no existe en la base de datos.")

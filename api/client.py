import requests

class AviasalesAPI:
    def __init__(self, base_url="https://api.aviasales.ru"):
        self.base_url = base_url

    def search_tickets(self, origin, destination):
        response = requests.get(
            f"{self.base_url}/search",
            params={"from": origin, "to": destination}
        )
        return response

    def get_prices(self, ticket_id):
        response = requests.get(f"{self.base_url}/prices/{ticket_id}")
        return response
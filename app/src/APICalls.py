import requests

class APICall:
    def __init__(self, ip: str) -> None:
        self.url = f"http://{ip}:8000/"
        self.session = requests.Session()
        self.header = {"accept": "application/json", 
                       "Content-Type": "application/json"}
        
    def is_alive(self) -> bool:
        response = self.session.get(self.url)
        
        if response.status_code == 200:
            return True
        else:
            return False
    
    def add_games(self, json: dict):
        response = self.session.post(str(self.url + "games/add_game/"), headers=self.header, json=json)
        
        return response
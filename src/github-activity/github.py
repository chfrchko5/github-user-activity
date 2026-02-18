import requests
import json
import typer

app = typer.Typer(help='github event fetcher for specified users')

class Event():
    def __init__(self, github_name):
        self.name = github_name
    
    def fetch_github(self):
        res = requests.get(f'https://api.github.com/users/{self.name}/events')
        if res.status_code == 200:
            response = json.loads(res.text)
            print(f'--- latest events for user "{self.name}" ---')
        elif res.status_code == 404:
            print(f'github username {self.name} does not exist')
        else:
            print(f'could not fetch events for {self.name}')
        
        for object in response:
            print(
                f'- performed "{object['type']}" on repo "{object['repo']['name']}" at {object['created_at']}'
            )
        


# one action in typer
# to take a github username and then perform fetch_github() class method
@app.command(help="fetch and print out recent events of the specified user")
def fetch(username: str = typer.Argument(help='github username of whom to fetch the events')):
    fetching_user = Event(username)
    fetching_user.fetch_github()

if __name__ == "__main__":
    app()
players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33,
        "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32,
    "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "DeMar DeRozan",
    "age": 32,
    "position": "Shooting Guard",
    "team": "Chicago Bulls"
    }
]
kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
# Create your Player instances here!
LeBron={
    "name": "LeBron James", 
    "age":38,
    "position": "small forward", 
    "team": "Los Angeles Lakers"
}


class Player:
    team_list=[]
    def __init__(self,dictonary):
        self.name = dictonary["name"]
        self.age = dictonary["age"]
        self.position = dictonary["position"]
        self.team = dictonary["team"]
    @classmethod
    def get_team(cls, team_list):
        cls.team_list.append(Player(team_list))

kevin=Player(kevin)
jason=Player(jason)
kyrie=Player(kyrie)
LeBron=Player(LeBron)
new_team = []
for item in players:
    var=locals()
    print(var(item["name"]))
    new_team.append(Player(item))
print(new_team)
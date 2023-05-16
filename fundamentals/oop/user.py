class user:
    def __init__(self,first_name,last_name,email,age,is_rewards_member=False,gold_card_points = 0):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.is_rewards_member=is_rewards_member
        self.gold_card_points=gold_card_points
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
    def enroll(self):
        if not self.is_rewards_member :
            self.is_rewards_member=True
            self.gold_card_points=200
            return True
        if self.is_rewards_member :
            print("User already a member.")
    def spend_points(self, amount):
        if self.gold_card_points - amount >=0:
            self.gold_card_points=self.gold_card_points - amount
            print(f"your have now {self.gold_card_points} poins")
        if self.gold_card_points - amount <0:
            print("you don't have enough points" )
user3=user("aymen","ben moussa","aymen@gmail.com",24,True,8)
#aymen.display_info()
user1=user("ali","hsouna","ali@gmail.com",28,False)
user2=user("aziz","med saleh","aziz@gmail.com",19,True,300)

user1.display_info()
user1.enroll()
user1.spend_points(50)
user1.display_info()
user2.enroll()
user2.spend_points(80)
user2.display_info()


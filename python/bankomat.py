users = {
  "Adam": {
    "password": "123",
    "money": 300,
  },
  "David": {
    "password": "456",
    "money": 400,
  },
}

while True:
  uinput = str(input())

  if uinput == "deposit":
    amount = float(input("How much? "))
    name = str(input("Who's account should the money be deposited to? "))

    if name in users and amount > 0:
      users[name]["money"] += amount
      print(f"Deposited {amount} to {name}'s account. Account now has {users[name]['money']} ready to withdraw.")
    else:
      print("Error: invalid username or deposition amount")
  
  elif uinput == "withdraw":
    amount = float(input("How much? "))
    name = str(input("Who's account should the money be withdrawn from? "))

    if name in users and amount > 0 and amount <= users[name]["money"]:
      password = str(input("Type the account password to proceed: "))
      if password == users[name]["password"]:
        users[name]["money"] -= amount
        
        print(f"Withdrew {amount} from {name}'s account. Account now has {users[name]['money']} left.")
      else:
        print("Error: incorrect password")

    else:
      print("Error: invalid username or withdrawal amount")

  elif uinput == "balance":
    name = str(input("Who's account should be checked? "))
    if name in users:
      password = str(input("Type the account password to proceed: "))
      if password == users[name]["password"]:
        print(f"Account has {users[name]['money']} ready to withdraw.")
      else:
        print("Error: incorrect password")

    else:
      print("Error: invalid username")
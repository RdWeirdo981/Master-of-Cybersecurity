import Server

# Test Add Shares
print("- Add Share Test -")
alice_add = Server.ADDServer()
bob_add = Server.ADDServer()
alice_private = int(input("Please enter Alice's private input: "))
bob_private = int(input("Please enter Bob's private input: "))
alice_add.set_private_input(alice_private)
bob_add.set_private_input(bob_private)

Add_test = Server.AriAdd(alice_add, bob_add)
Add_test.do_calculate()
print("Alice result: ", alice_add.result)
print("Bob result: ", bob_add.result)
# import
import random

mod_number = 2**16

# server type
class ADDServer:
    def __init__(self):
        self.private_input = None
        self.own_shares = None # x0,x1
        self.others_share = None # y0
        self.calculation_seed = None #z0
        self.result = None

    def get_private_input(self):
        return self.private_input
    def get_own_shares(self):
        return self.own_shares
    def get_others_shares(self):
        return self.others_shares
    def get_calculation_seed(self):
        return self.calculation_seed
    def get_result(self):
        return self.result

    def set_private_input(self,private_input):
        self.private_input = private_input
        return True
    def set_own_shares(self, own_shares):
        self.own_shares = own_shares
        return True
    def set_others_shares(self, others_shares):
        self.others_shares = others_shares
        return True
    def set_calculation_seed(self, calculation_seed):
        self.calculation_seed = calculation_seed
        return True
    def set_result(self, result):
        self.result = result
        return True
class MulServer:
    def __init__(self):
        self.private_input = None
        self.own_shares = None # x0,x1
        self.others_share = None # y0
        self.random_pair = None # a0, b0
        self.calculation_seed = None # e0, f0, e1, f1, e, f, c0
        self.result = None # c

    def get_private_input(self):
        return self.private_input
    def get_own_shares(self):
        return self.own_shares
    def get_others_shares(self):
        return self.others_shares
    def get_random_pair(self):
        return self.random_pair
    def get_calculation_seed(self):
        return self.calculation_seed
    def get_result(self):
        return self.result

    def set_private_input(self,private_input):
        self.private_input = private_input
        return True
    def set_own_shares(self, own_shares):
        self.own_shares = own_shares
        return True
    def set_others_shares(self, others_shares):
        self.others_shares = others_shares
        return True
    def set_random_pair(self, random_pair):
        self.random_pair = random_pair
        return True
    def set_calculation_seed(self, calculation_seed):
        self.calculation_seed.append(calculation_seed)
        return True
    def set_result(self, result):
        self.result = result
        return True



# calculation type

class AriAdd:
    def __init__(self, alice, bob):
        self.alice = alice
        self.bob = bob

    def generate_random_shares(self, server):
        r = random.randint(1, server.private_input)
        own_shares = []
        own_shares.append(r % mod_number)
        own_shares.append((server.private_input - r) % mod_number)
        server.set_own_shares(own_shares)

    def exchange_shares(self):
        bob_share = self.bob.get_own_shares()
        alice_share = self.alice.get_own_shares()
        self.alice.set_others_shares(bob_share[0])
        self.bob.set_others_shares(alice_share[1])

    def calculate_add(self):
        z0 = (self.alice.get_own_shares()[0] + self.alice.get_others_shares()) % mod_number
        z1 = (self.bob.get_own_shares()[1] + self.bob.get_others_shares()) % mod_number
        self.alice.set_calculation_seed(z0)
        self.bob.set_calculation_seed(z1)

    def generate_result(self):
        result = self.alice.get_calculation_seed() + self.bob.get_calculation_seed()
        self.alice.set_result(result)
        self.bob.set_result(result)

    def do_calculate(self):
        self.generate_random_shares(self.alice)
        self.generate_random_shares(self.bob)
        self.exchange_shares()
        self.calculate_add()
        self.generate_result()

class AriMul:
    def __init__(self, alice, bob):
        self.alice = alice
        self.bob = bob

    def generate_random_shares(self, server):
        r = random.randint(1, server.private_input)
        own_shares = []
        own_shares.append(r % mod_number)
        own_shares.append((server.private_input - r) % mod_number)
        server.set_own_shares(own_shares)

    def generate_random_seed(self):
        c = random.randint(1, mod_number-1)
        flag_int = False
        while not flag_int:
            a = random.randint(1, c)
            if a % c == 0:
                flag_int = True
        b = a % c


        a0 = random.randint(1, a)
        a1 = (a - a0) % mod_number
        b0 = random.randint(1, b)
        b1 = (b - b0) % mod_number

        alice_random_seed = []
        bob_random_seed = []

        alice_random_seed.append(a0)
        alice_random_seed.append(b0)
        bob_random_seed.append(a1)
        bob_random_seed.append(b1)

        self.alice.set_random_pair(alice_random_seed)
        self.bob.set_random_pair(bob_random_seed)

    def exchange_shares(self):
        bob_share = self.bob.get_own_shares()
        alice_share = self.alice.get_own_shares()
        self.alice.set_others_shares(bob_share[0])
        self.bob.set_others_shares(alice_share[1])

    def calculate_ef(self):
        e0 = self.alice.get_own_shares()[0] - self.alice.get_random_pair()[0]
        self.alice.set_calculation_seed(e0)
        f0 = self.alice.get_others_shares() - self.alice.get_random_pair()[1]
        self.alice.set_calculation_seed(f0)

        e1 = self.bob.get_own_shares()[1] - self.bob.get_random_pair()[0]
        self.bob.set_calculation_seed(e1)
        f1 = self.bob.get_others_shares() - self.bob.get_random_pair()[1]
        self.bob.set_calculation_seed(f1)

        # exchange
        self.alice.set_calculation_seed(e1)
        self.alice.set_calculation_seed(f1)
        self.bob.set_calculation_seed(e0)
        self.bob.set_calculation_seed(f0)

        # cal
        ef_alice = self.alice.get_calculation_seed[0] + self.alice.get_calculation_seed[1] \
                   + self.alice.get_calculation_seed[2] + self.alice.get_calculation_seed[3]
        ef_bob = self.bob.get_calculation_seed[0] + self.bob.get_calculation_seed[1] \
                   + self.bob.get_calculation_seed[2] + self.bob.get_calculation_seed[3]

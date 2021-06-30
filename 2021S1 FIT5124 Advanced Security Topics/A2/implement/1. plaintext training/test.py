import torch

weight1 = torch.load("./fc1_weight.pt")
weight2 = torch.load("./fc2_weight.pt")
weight3 = torch.load("./fc3_weight.pt")

bias1 = torch.load("./fc1_bias.pt")
bias2 = torch.load("./fc2_bias.pt")
bias3 = torch.load("./fc3_bias.pt")

print("weight1: ", len(weight1[1]), " * ", len(weight1))
print("weight2: ", len(weight2[1]), " * ", len(weight2))
print("weight3: ", len(weight3[1]), " * ", len(weight3))

print("bias1: ", len(bias1))
print("bias2: ", len(bias2))
print("bias3: ", len(bias3))


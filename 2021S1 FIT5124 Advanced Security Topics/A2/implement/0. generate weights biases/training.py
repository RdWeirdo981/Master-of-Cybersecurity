# Reference: https://blog.csdn.net/hxxjxw/article/details/105667269

import torch
import torchvision
from torchvision import transforms
from torch.nn import functional as F
from torch import optim
from utils import one_hot
import net


batch_size = 512
# num of picture / time

transform = transforms.Compose([
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize((0.5,), (0.5,))
])

trainset = torchvision.datasets.MNIST(
    root='./data/FashionMNIST',
    train=True,
    download=True,
    transform=transform
)

train_loader = torch.utils.data.DataLoader(
    dataset=trainset,
    batch_size=batch_size,
    shuffle=True
)

testset = torchvision.datasets.MNIST(
    root='./data/FashionMNIST',
    train=False,
    download=True,
    transform=transform
)

test_loader = torch.utils.data.DataLoader(
    dataset=testset,
    batch_size=batch_size,
    shuffle=True
)

model = net.Net()  # Create a model

# [w1, b1, w2, b2, w3, b3] initialize weights & biases
optimizer = optim.SGD(model.parameters(), lr=1e-2, momentum=0.9)

train_loss = []

for epoch in range(3):

    for idx, data in enumerate(train_loader):
        inputs, labels = data
        inputs = inputs.view(inputs.size(0), 28 * 28)
        outputs = model(inputs)
        labels_onehot = one_hot(labels)
        loss = F.mse_loss(outputs, labels_onehot)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        train_loss.append(loss.item())
        if idx % 10 == 0:
            print(epoch, idx, loss.item())


total_correct = 0

for idx, data in enumerate(test_loader):
    inputs, labels = data
    inputs = inputs.view(inputs.size(0), 28 * 28)

    outputs = model(inputs)
    pred = outputs.argmax(dim=1)
    correct = pred.eq(labels).sum().float().item()

    total_correct += correct

accuracy = total_correct / len(test_loader.dataset)
print('test accuracy: ', accuracy)



dic = model.state_dict()
key = dic.keys()
print(key)

torch.save(model.state_dict(), "./model.pt")

# obtain weights & biases
output_1_bias = model.fc1.bias.data
output_1_weight = model.fc1.weight.data
save_1_bias = torch.save(output_1_bias, "./fc1_bias.pt")
save_1_weight = torch.save(output_1_weight, "./fc1_weight.pt")

output_2_bias = model.fc2.bias.data
output_2_weight = model.fc2.weight.data
save_2_bias = torch.save(output_2_bias, "./fc2_bias.pt")
save_2_weight = torch.save(output_2_weight, "./fc2_weight.pt")

output_3_bias = model.fc3.bias.data
output_3_weight = model.fc3.weight.data
save_3_bias = torch.save(output_3_bias, "./fc3_bias.pt")
save_3_weight = torch.save(output_3_weight, "./fc3_weight.pt")
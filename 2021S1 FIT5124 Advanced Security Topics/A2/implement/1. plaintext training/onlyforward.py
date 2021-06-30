# Reference: https://blog.csdn.net/hxxjxw/article/details/105667269

import torch
import torchvision
from torchvision import transforms
import net


transform = transforms.Compose([
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize((0.5,), (0.5,))
])

testset = torchvision.datasets.MNIST(
    root='./data/FashionMNIST',
    train=False,
    download=True,
    transform=transform
)

test_loader = torch.utils.data.DataLoader(
    dataset=testset,
    shuffle=True
)

# load model
model = net.Net()  # Create a model
model.load_state_dict(torch.load("./model.pt"))
model.eval()


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

# dic = model.state_dict()
# key = dic.keys()
# print(key)
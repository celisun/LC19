import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(128, 256, 1)
        self.conv2 = nn.Conv2d(128, 256, 3, padding=1)
        self.conv3 = nn.Conv2d(128, 256, 5, padding=2)
        self.max_pooling = nn.MaxPool2d(3, stride=1, padding=1)

    def forward(self, x):
        out1 = F.relu(self.conv1(x))  # 1,256, 14, 14
        out2 = F.relu(self.conv2(x)) # 1, 256, 14, 14
        out3 = F.relu(self.conv3(x))  # 1, 256, 14, 14
        out_max = self.max_pooling(x)  # 1,128, 14, 14

        output = torch.cat((out1, out2, out3, out_max), dim=1)
        return output


def function(x, y):
    x, y = torch.tensor(x, requires_grad=True), torch.tensor(y, requires_grad=True)
    loss = 2 * x * y + x ** 2
    loss.backward()
    return x.grad

print (function(3, 1))



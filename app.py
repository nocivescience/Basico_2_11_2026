import torch as th
obs = th.tensor([[0.2, 0.9]])
W1 = th.tensor([
    [1., -1.],
    [-1., 1]
])
W2 = th.tensor([
    [-1.],
    [1.]
])
paso1 = obs @ W1
h = th.tanh(paso1)
paso2 = h @ W2
print(paso2)
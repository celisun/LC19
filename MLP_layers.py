import numpy as np

class Layer:
    def __init__(self):
        pass

    def forward(self, input):
        return input

    def backward(self, input, grad_output):
        # chain rule is d_loss/d_layer * d_layer/d_x
        num_units = input.shape[1]
        d_layer_d_input = np.eye(num_units)
        return np.dot(grad_output, d_layer_d_input)


class ReLU(Layer):
    def forward(self, input):
        # rectified nonlinear f(x):
        # 0 if x < 0
        # x otherwise
        return np.maximum(0, input)

    def backward(self, input, grad_output):
        # 0 if x < 0, 1 otherwise
        relu_grad = input > 0
        return grad_output * relu_grad


class Dense(Layer):
    def __init__(self, n_input, n_output, learning_rate=0.1):
        self.learning_rate = learning_rate
        self.weights = np.random.normal(loc=0.0,
                            scale=np.sqrt(2/(n_input+n_output)),
                            size=(n_input, n_output))
        self.biases = np.zeros(n_output)

    def forward(self, input):
        # w_t * x + b
        return np.dot(input, self.weights) + self.biases # N, n_output

    def backward(self, input, grad_output):
        # dx_d layer: output * w
        grad_input = np.dot(grad_output, self.weights.T) # N, n_input
        # dw d layer: output * x
        grad_weights = np.dot(input.T, grad_output) # n_input, n_output
        # db d layer: output
        grad_biases = grad_output.mean(axis=0) * input.shape[0]  # N, n_output

        assert grad_weights.shape == self.weights.shape \
                and grad_biases.shape == self.biases.shape

        # stochastic gradient descent step
        self.weights -= self.learning_rate * grad_weights
        self.biases -= self.learning_rate * grad_biases

        return grad_input   # pass for previous layer


network = [
    Dense(32*32*3, 100),
    ReLU(),
    Dense(100, 200),
    ReLU(),
    Dense(200,10)
]


def softmax_cross_entropy_with_logits(logits, y):
    logits_y = logits[np.arrange(len(logits), y)]  # pick target score for right class
    xentropy = - logits_y + np.log(np.sum(np.exp(logits), axis=-1)) # probability

    return xentropy


def grad_softmax_cross_entropy_with_logits(logits, y):
    # one_hot y distribution p
    ones_y = np.zeros_like(logits)
    ones_y[np.arange(len(logits)), y] = 1

    softmax = np.exp(logits) / np.exp(logits).sum(axis=-1, keepdims=True)

    # - y + p  / N
    return (- ones_y + softmax) / logits.shape[0]


def forward(network, X):
    activations, input = [], X

    # forward and store each output
    for l in network:
        activations += [l.forward(input)]
        input = activations[-1]

    assert  len(activations) == len(network)
    return activations


def predict(network, X):
    logits = forward(network, X)[-1]
    return logits.argmax(axis=-1)


def train(network, X, y):
    layer_activations = forward(network, X)
    layer_inputs = [X] + layer_activations
    logits = layer_activations[-1]

    # get loss output
    # loss = softmax_cross_entropy_with_logits(logits, y)
    # gradient w.r.t loss output f(x)
    loss_grad = grad_softmax_cross_entropy_with_logits(logits, y)

    # back prop. compute gradient and update
    for i, layer in enumerate(network)[::-1]:
        loss_grad = layer.backward(layer_inputs[i], loss_grad)

    return np.mean(loss)


for e in range(25):
    for x_batch, y_batch in iterate_minibatches(X_train, y_train, batchsize=32):
         train(network, x_batch, y_batch)









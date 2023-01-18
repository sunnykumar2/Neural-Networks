
import numpy as np


def softmax(a):
    e_pa = np.exp(a)  # Vector
    ans = e_pa/np.sum(e_pa, axis=1, keepdims=True)
    return ans


class NeuralNetwork:

    def __init__(self, input_size, layers, output_size):
        np.random.seed(0)

        model = {}  # Dictionary

        # First Layer
        model['W1'] = np.random.randn(input_size, layers[0])
        model['b1'] = np.zeros((1, layers[0]))

        # Second Layer
        model['W2'] = np.random.randn(layers[0], layers[1])
        model['b2'] = np.zeros((1, layers[1]))

        # Third/Output Layer
        model['W3'] = np.random.randn(layers[1], output_size)
        model['b3'] = np.zeros((1, output_size))

        self.model = model
        self.activation_outputs = None

    def forward(self, x):

        W1, W2, W3 = self.model['W1'], self.model['W2'], self.model['W3']
        b1, b2, b3 = self.model['b1'], self.model['b2'], self.model['b3']

        z1 = np.dot(x, W1) + b1
        a1 = np.tanh(z1)

        z2 = np.dot(a1, W2) + b2
        a2 = np.tanh(z2)

        z3 = np.dot(a2, W3) + b3
        y_ = softmax(z3)

        self.activation_outputs = (a1, a2, y_)
        return y_

    def backward(self, x, y, learning_rate=0.001):
        W1, W2, W3 = self.model['W1'], self.model['W2'], self.model['W3']
        b1, b2, b3 = self.model['b1'], self.model['b2'], self.model['b3']
        m = x.shape[0]

        a1, a2, y_ = self.activation_outputs

        delta3 = y_ - y
        dw3 = np.dot(a2.T, delta3)
        db3 = np.sum(delta3, axis=0)

        delta2 = (1-np.square(a2))*np.dot(delta3, W3.T)
        dw2 = np.dot(a1.T, delta2)
        db2 = np.sum(delta2, axis=0)

        delta1 = (1-np.square(a1))*np.dot(delta2, W2.T)
        dw1 = np.dot(x.T, delta1)
        db1 = np.sum(delta1, axis=0)

        # Update the Model Parameters using Gradient Descent
        self.model["W1"] -= learning_rate*dw1
        self.model['b1'] -= learning_rate*db1

        self.model["W2"] -= learning_rate*dw2
        self.model['b2'] -= learning_rate*db2

        self.model["W3"] -= learning_rate*dw3
        self.model['b3'] -= learning_rate*db3

        # :)

    def predict(self, x):
        y_out = self.forward(x)
        return np.argmax(y_out, axis=1)

        def summary(self):
            W1, W2, W3 = self.model['W1'], self.model['W2'], self.model['W3']
            a1, a2, y_ = self.activation_outputs

            print("W1 ", W1.shape)
            print("A1 ", a1.shape)

            print("W2 ", W2.shape)
            print("A2 ", a2.shape)

            print("W3 ", W3.shape)
            print("Y_ ", y_.shape)


def loss(y_oht, p):
    l = -np.mean(y_oht*np.log(p))
    return l


def one_hot(y, depth):
    m = y.shape[0]
    y_oht = np.zeros((m, depth))
    y_oht[np.arange(m), y] = 1
    return y_oht


def train(X, Y, model, epochs, learning_rate, logs=True):
    training_loss = []

    classes = 2
    Y_OHT = one_hot(Y, classes)

    for ix in range(epochs):

        Y_ = model.forward(X)
        l = loss(Y_OHT, Y_)
        training_loss.append(l)
        model.backward(X, Y_OHT, learning_rate)

    if(logs):
        print("Epoch %d Loss %.4f" % (ix, l))

    return training_loss


x = [[1, 1],
     [1, -1],
     [-1, 1],
     [-1, -1]]
y = [-1, 1, -1, 1]
x = np.asarray(x)
y = np.asarray(y)
model = NeuralNetwork(input_size=2, layers=[10, 5], output_size=2)
for i in range(1, 101):
    losses = train(x, y, model, i, 0.001)

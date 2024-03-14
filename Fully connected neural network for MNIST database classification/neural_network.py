import numpy as np

class NeuronsLayer:
    def __init__(self, input_size, output_size) -> None:
        """
        output_size- number of neurons in layer
        input_size- size of input from which every neuron in this layer will read
        """

        # assigning random values in range [-0.5, 0.5] to weight and bias
        self.weights = np.random.rand(input_size, output_size) - 0.5
        self.bias = np.random.rand(1, output_size) - 0.5

    def pass_forward(self, input):
        self.input = input
        self.output = np.dot(self.input, self.weights) + self.bias
        return self.output

    def propagate_backwards(self, output_gradients, learning_rate):
        # calculating gradients
        input_gradients = np.dot(output_gradients, self.weights.T)
        weights_gradients = np.dot(self.input.T, output_gradients)
        bias_gradients = output_gradients

        # update weights and biases
        self.weights -= learning_rate * weights_gradients
        self.bias -= learning_rate * bias_gradients

        # return dE/dX that will be dE/dY for previous layer
        return input_gradients


class ActivationLayer:
    def __init__(self, activation_func, activation_func_derivative):
        self.activation_func = activation_func
        self.activation_func_derivative = activation_func_derivative

    def pass_forward(self, input_data):
        self.input = input_data
        self.output = self.activation_func(self.input)
        return self.output

    def propagate_backwards(self, output_error, learning_rate):
        return self.activation_func_derivative(self.input) * output_error


class Network:
    def __init__(self, loss_func, loss_func_derivative):
        self.layers = []
        self.loss_func = loss_func
        self.loss_func_derivative = loss_func_derivative

    # add layer to network
    def add(self, layer):
        self.layers.append(layer)

    # predict output for given input
    def predict(self, input_data):
        samples = len(input_data)
        result = []

        # run network over all samples
        for i in range(samples):
            # forward propagation
            output = input_data[i]
            for layer in self.layers:
                output = layer.pass_forward(output)
            result.append(output)

        return result

    # train the network
    def fit(self, x_train, y_train, epochs, learning_rate):
        samples = len(x_train)

        # training loop
        for i in range(epochs):
            for j in range(samples):
                # forward propagation
                output = x_train[j]
                for layer in self.layers:
                    output = layer.pass_forward(output)

                # backward propagation
                error = self.loss_func_derivative(y_train[j], output)
                for layer in reversed(self.layers):
                    error = layer.propagate_backwards(error, learning_rate)



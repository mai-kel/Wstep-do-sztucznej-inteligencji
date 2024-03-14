import numpy as np
import matplotlib.pyplot as plt


class SVM:
    def __init__(self, beta=0.001, lambda_param=0.01, iterations=1000, num_to_learn=0):
        self.beta = beta
        self.lambda_param = lambda_param
        self.n_iters = iterations
        self.w = None
        self.b = None
        self.num_to_learn = num_to_learn


    def fit(self, X, y):
        n_samples, n_features = X.shape

        y_scaled = np.where(y == self.num_to_learn, 1, -1)

        self.w = np.zeros(n_features)
        self.b = 0

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                condition = y_scaled[idx] * (np.dot(x_i, self.w) - self.b) >= 1
                if condition:
                    self.w -= self.beta * (2 * self.lambda_param * self.w)
                else:
                    self.w -= self.beta * (2 * self.lambda_param * self.w - np.dot(x_i, y_scaled[idx]))
                    self.b -= self.beta * y_scaled[idx]


    def predict(self, X):
        approx = np.dot(X, self.w) - self.b
        return np.sign(approx)

    def get_approx(self, X):
        return np.dot(X, self.w) - self.b

class MegaSVM:
    def __init__(self, beta=0.001, lambda_param=0.01, iterations=1000) -> None:
        self.beta = beta
        self.lambda_param = lambda_param
        self.iterations = iterations
        self.w = None
        self.b = None
        self.svms_list = [SVM(beta, lambda_param, iterations, i) for i in range(10)]

    def fit(self, X, y):
        for svm in self.svms_list:
            svm.fit(X, y)

    def predict(self, X):
        approxes = [svm.get_approx(X) for svm in self.svms_list]
        return approxes.index(max(approxes))

    def predict_multiple(self, X):
        prediciotns = []
        for x in X:
            prediciotns.append(self.predict(x))
        return prediciotns

    def get_accuracy(self, true, predicted):
        correct = 0
        all = len(true)
        for i in range(len(true)):
            correct += 1 if true[i]==predicted[i] else 0
        return correct/all


def plot_confusion_matrix(confusion_matrix, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.figure()
    plt.imshow(confusion_matrix, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    plt.tight_layout()
    plt.xticks([i for i in range(10)])
    plt.yticks([i for i in range(10)])
    for (j,i),label in np.ndenumerate(confusion_matrix):
        plt.text(i,j,label,ha='center',va='center')
        plt.text(i,j,label,ha='center',va='center')
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()


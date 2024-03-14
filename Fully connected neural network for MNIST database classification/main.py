from matplotlib import pyplot as plt
import numpy as np
import argparse
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import tensorflow as tf
from neural_network import Network, NeuronsLayer, ActivationLayer
from activation_func import tg, tg_derivative
from loss_func import loss_func, loss_func_derivative
from keras.utils import to_categorical



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

def convert_output_vector_to_number(vector):
    return list(vector).index(max(vector))

def convert_entire_output_to_numbers(output):
    new_output = []
    for vector in output:
        new_output.append()


if __name__ == "__main__":

    # getting params
    parser = argparse.ArgumentParser()
    parser.add_argument('to_train', type=int)
    parser.add_argument('to_test', type=int)
    args = parser.parse_args()
    to_train = int(args.to_train)
    to_test = int(args.to_test)

    # loading MNIST database
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

    # changing images format from 28x28 matrix to 784 length vector and scaling pixels
    train_images = np.reshape(train_images, (train_images.shape[0], 1, 28*28))/255
    test_images = np.reshape(test_images, (test_images.shape[0], 1, 28*28))/255

    # changing labels from numbers to 10 element vector
    # for example 2 is transformed to [0, 0, 1, 0, ..., 0]
    train_labels = to_categorical(train_labels)

    # selecting random indexes that will be used to choose random sample of images to test and train
    random_indexes_train = np.random.choice(len(train_images), to_train)
    random_indexes_test = np.random.choice(len(test_images), to_test)

    # choosing random sample of training data
    train_images_sample = train_images[random_indexes_train]
    train_labels_sample = train_labels[random_indexes_train]

    # choosing random sample of testing data
    test_images_sample = test_images[random_indexes_test]
    test_labels_sample = test_labels[random_indexes_test]

    neural_network = Network(loss_func, loss_func_derivative)
    neural_network.add(NeuronsLayer(28*28, 100))                # input_shape=(1, 28*28)    ;   output_shape=(1, 100)
    neural_network.add(ActivationLayer(tg, tg_derivative))
    neural_network.add(NeuronsLayer(100, 50))                   # input_shape=(1, 100)      ;   output_shape=(1, 50)
    neural_network.add(ActivationLayer(tg, tg_derivative))
    neural_network.add(NeuronsLayer(50, 10))                    # input_shape=(1, 50)       ;   output_shape=(1, 10)
    neural_network.add(ActivationLayer(tg, tg_derivative))

    neural_network.fit(train_images_sample, train_labels_sample, 50, 0.1)

    y_predicted = neural_network.predict(test_images_sample)
    # changing labels from 10 element vectors to numbers
    # for example [0.1, 0.8, 0.2, 0.15, 0.12, 0.23, 0.18, 0.11, 0.13, 0.03] is converted to 1
    y_predicted_classes = np.asarray([np.argmax(vector) for vector in y_predicted])

    acc = accuracy_score(test_labels_sample, y_predicted_classes)
    conf_matrix = confusion_matrix(test_labels_sample, y_predicted_classes)
    class_report = classification_report(test_labels_sample, y_predicted_classes)

    print("Accuracy:", acc)
    print("")
    print("Confusion matrix")
    print(conf_matrix)
    print("")
    print("Classification Report")
    print("")
    print(class_report)
    plot_confusion_matrix(conf_matrix)



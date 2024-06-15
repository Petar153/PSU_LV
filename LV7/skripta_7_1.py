import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix


# MNIST podatkovni skup
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# TODO: prikazi nekoliko slika iz train skupa

def display_sample_images(x_data, y_data, num_samples=5):
    plt.figure(figsize=(10, 2))
    for i in range(num_samples):
        plt.subplot(1, num_samples, i + 1)
        plt.imshow(x_data[i], cmap='gray')
        plt.title(f"Label: {y_data[i]}")
        plt.axis('off')
    plt.show()

display_sample_images(x_train, y_train)

# Skaliranje vrijednosti piksela na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# Slike 28x28 piksela se predstavljaju vektorom od 784 elementa
x_train_s = x_train_s.reshape(60000, 784)
x_test_s = x_test_s.reshape(10000, 784)

# Kodiraj labele (0, 1, ... 9) one hot encoding-om
y_train_s = keras.utils.to_categorical(y_train, 10)
y_test_s = keras.utils.to_categorical(y_test, 10)


# TODO: kreiraj mrezu pomocu keras.Sequential(); prikazi njenu strukturu pomocu .summary()

model = Sequential([
    Flatten(input_shape=(28, 28)),      
    Dense(128, activation='relu'),    
    Dense(64, activation='relu'),      
    Dense(10, activation='softmax')    
])

# TODO: definiraj karakteristike procesa ucenja pomocu .compile()

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


# TODO: provedi treniranje mreze pomocu .fit()

history = model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.2)


# TODO: Izracunajte tocnost mreze na skupu podataka za ucenje i skupu podataka za testiranje

train_loss, train_accuracy = model.evaluate(x_train, y_train, verbose=0)
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)

print(f"Train accuracy: {train_accuracy:.4f}")
print(f"Test accuracy: {test_accuracy:.4f}")

# TODO: Prikazite matricu zabune na skupu podataka za testiranje

y_train_pred = model.predict(x_train)
y_test_pred = model.predict(x_test)




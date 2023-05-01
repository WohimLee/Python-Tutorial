import random
import numpy as np
import matplotlib.pyplot as plt

def train(x:np.ndarray, y:np.ndarray, epochs=1000, lr=1e-2):

    k = 2 #random.random()
    b = 0

    plt.figure()
    axis_x = [x.min()-0.1, x.max()+0.1]
    axis_y = [y.min()-0.1, y.max()+0.1]
    for i in range(epochs):

        predict = k * x + b
        loss = np.sum((predict - y)** 2 * 0.5)

        delta_k = np.sum((y - predict) * (-x))
        delta_b = np.sum((y - predict) * (-1))

        k = k - lr * delta_k
        b = b - lr * delta_b

        tx = np.array(axis_x)
        ty = k * tx + b

        if (i + 1) % 100 == 0 or i < 3:
            #print("Iter %d : error=%f, k = %f, b = %f" % (i, err, k, b))
            plt.clf()
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title("Iter %d : loss=%f, k = %f, b = %f" % (i, loss, k, b))
            plt.plot(x, y, ".")
            plt.plot(tx, ty, 'g-')
            plt.axis(axis_x+axis_y)
            plt.pause(0.5)

    return (k, b)


if __name__ == '__main__':
        
    #我们定义房价数据
    x = np.arange(10, dtype=np.float32).reshape(10, 1) + 2010
    y = np.array([[1.8, 2.1, 2.3, 2.3, 2.85, 3.0, 3.3, 4.9, 5.45, 5.0]], dtype=np.float32).T

    #数据归一化
    x_mean = x.mean()
    y_mean = y.mean()
    x_std  = x.std()
    y_std  = y.std()
    
    x = (x - x_mean) / x_std
    y = (y - y_mean) / y_std

    #梯度下降法求解
    k, b = train(x, y)

    #估算2019年的房价多少
    #归一化
    x_2019 = (2019 - x_mean) / x_std
    y_2019 = x_2019 * k + b

    #结果反归一化
    y_2019 = y_2019 * y_std + y_mean
    print("模型的参数是: k=%f, b=%f, 预估的2019房价为: %f 万元" % (k, b, y_2019))
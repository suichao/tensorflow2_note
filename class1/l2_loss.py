import tensorflow as tf
import numpy as np
x = np.random.random([3, 3])
x1 = np.concatenate(x)
print(x)
output = sum(x1 ** 2) / 2
print(output)
res = tf.nn.avg_pool
print(res)
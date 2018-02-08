'''
2018/0205
logistic regression 3.4.3  p093
tensorlow /orgate

１モデル定義
２誤差関数の定義
３最適化手法の定義
４初期化
5 学習

'''

import numpy as np
import tensorflow as tf

tf.set_random_seed(0)

w = tf.Variable(tf.zeros([2,1]))
b = tf.Variable(tf.zeros([1]))

x = tf.placeholder(tf.float32, shape=[None, 2])
t = tf.placeholder(tf.float32, shape=[None,1])
y = tf.nn.sigmoid(tf.matmul(x,w) + b)

cross_entropy = - tf.reduce_sum(t * tf.log(y) + (1 - t) * tf.log(1 - y))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

correct_prediction = tf.equal(tf.to_float(tf.greater(y,0.5)),t)

'''
モデル学習
xor
'''
X = np.array([[0,0],[0,1],[1,0],[1,1]])
Y = np.array([[0],[1],[1],[1]])

# initialization
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# learning
for epoch in range(200):
    sess.run(train_step, feed_dict= {
    x: X,
    t: Y
    }
    )

# learning result
classified = correct_prediction.eval(session=sess, feed_dict= {
   x: X,
   t: Y
})

proba = y.eval(session=sess, feed_dict={
    x: X,
    t: Yprob = y.eval(session=sess, feed_dict={
    x: X,
    t: Y
})
})
print('classified:')
print(classified)

print('output probability:')
print(proba)

print ('w:', sess.run(w))
print ('b:', sess.run(b))

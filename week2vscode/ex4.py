import tensorflow as tf

# constant of 1d tensor (vector)
a = tf.constant([2, 2], name="vector")
# constant of 2x2 tensor (matrix)
b = tf.constant([[0, 1], [2, 3]], name="b")
x = tf.add(a, b, name="add")

with tf.Session() as session:
    # สร้างไฟล์
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(x))
    # tf.Session.run(fetches, feed_dict=None, options=None, run_metadata=None)
    # tf.constant(value, dtype=None, shape=None, name='Const', verify_shape=False)
writer.close()

# คือคำสั่ง tensorboard --logdir ./graphs คือการรัน ไฟล์ให้ไป localhost:6006
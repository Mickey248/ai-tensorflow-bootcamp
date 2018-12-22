import tensorflow as tf

a = tf.constant([2, 2], name="a")
b = tf.constant([3, 6], name="b")
x = tf.add(a, b, name="add")

with tf.Session() as session:
    # สร้างไฟล์
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(x))
    # tf.Session.run(fetches, feed_dict=None, options=None, run_metadata=None)
    # tf.constant(value, dtype=None, shape=None, name='Const', verify_shape=False)
writer.close()

# คือคำสั่ง tensorboard --logdir ./graphs คือการรัน ไฟล์ให้ไป localhost:6006
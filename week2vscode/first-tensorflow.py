import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a, b)

with tf.Session() as session:
    # สร้างไฟล์
    writer = tf.summary.FileWriter('./graphs', session.graph)
    # print(session.run(x))
    # print(session.run(tf.ones_like(x))

writer.close()

# คือคำสั่ง tensorboard --logdir ./graphs คือการรัน ไฟล์ให้ไป localhost:6006
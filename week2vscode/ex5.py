import tensorflow as tf

# x = tf.zeros(shape, type=tf.float32,name=None)

x = tf.zeros([2, 3], tf.int32) 

# ==> [[0, 0, 0], [0, 0, 0]]

with tf.Session() as session:
    # สร้างไฟล์
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(x))
writer.close()

# คือคำสั่ง tensorboard --logdir ./graphs คือการรัน ไฟล์ให้ไป localhost:6006
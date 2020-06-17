# 计算平均梯度的函数，该函数全网统一
def average_gradients(tower_grads):
    """Calculate the average gradient for each shared variable across all towers.
    Note that this function provides a synchronization point across all towers.
    Args:
      tower_grads: List of lists of (gradient, variable) tuples. The outer list
        is over individual gradients. The inner list is over the gradient
        calculation for each tower.
    Returns:
       List of pairs of (gradient, variable) where the gradient has been averaged
       across all towers.
    """
    average_grads = []
    for grad_and_vars in zip(*tower_grads):
        grads = []
        for g, _ in grad_and_vars:
            expend_g = tf.expand_dims(g, 0)
            grads.append(expend_g)
        grad = tf.concat(grads, 0)
        grad = tf.reduce_mean(grad, 0)
        v = grad_and_vars[0][1]
        grad_and_var = (grad, v)
        average_grads.append(grad_and_var)
    return average_grads

def train_multi_gpu():
    global graph
    # cpu里设置好输入占位符
    with graph.as_default(), tf.device('/cpu:0'):
        # input
        x = tf.placeholder(tf.float32, shape=[None, SPACE_I_DIMS, SPACE_J_DIMS, SPACE_K_DIMS, 1], name='x')
        y_ = tf.placeholder(tf.int64, shape=[None, 1])
        drop_rate = tf.placeholder(tf.float32)

        # learning rate
        global_step = tf.train.get_or_create_global_step()
        lr = tf.train.exponential_decay(
            lr0,
            global_step,
            decay_steps=lr_step,
            decay_rate=lr_decay,
            staircase=True)

        # optimaizer
        opt = tf.train.AdamOptimizer(learning_rate=lr)
		#用列表收集每个gpu的梯度
        tower_grad = []

        with tf.variable_scope(tf.get_variable_scope()):
            # gpu
            for i in range(NUM_GPUS):
                with tf.device('/gpu:%d' % i):
                    with tf.name_scope('gpu_%d' % i) as scope:
                        with tf.name_scope("tower_%d" % i):
                        	#每个gpu里放不同的数据
                            _x = x[i * batch_size:(i + 1) * batch_size]
                            _y = y_[i * batch_size:(i + 1) * batch_size]

                            # calculate inference
                            y = inference(_x, reuse=False, drop_rate=drop_rate)
                            # loss
                            mse_loss = tf.losses.mean_squared_error(_y, y)
                            cur_loss = mse_loss
							# 当前梯度
                            cur_grad = opt.compute_gradients(cur_loss)
                            tower_grad.append(cur_grad)
							#变量共享
                            tf.get_variable_scope().reuse_variables()
		#计算平均梯度
        grads = average_gradients(tower_grad)
        # 更新参数
        apply_grident_op = opt.apply_gradients(grads, global_step=global_step)
		#参数初始化
        init = tf.global_variables_initializer()

    # train steps
    with tf.Session(config=config).as_default() as sess:
        # init all variables
        init.run()
        try:
            for i in range(max_steps):

                # get next step data
                x_batch, y_batch, id, sex = sess.run(trian_next_batch)
           		#训练
                _ = sess.run(
                        [apply_grident_op], feed_dict={
                            x: x_batch,
                            y_: y_batch,
                            drop_rate: 0.2,
                        })
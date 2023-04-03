# result()
# 返回Task的执行结果。
# 如果Task已经完成，则返回Task封装的协程的执行结果（如果Task封装的协程引发异常，则重新引发该异常）。
# 如果Task已经取消，则该方法引发CancelledError异常。
# 如果Task的结果还不可用，该方法引发InvalidStateError异常。
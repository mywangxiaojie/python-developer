# You can do it easily by overriding the methods __call__ and after_return of the celery base task class.

# Following you see a piece of my code that uses a taskLogger class as context manager (with entry and exit point). The taskLogger class simply writes a line containing the task info in a mongodb instance.

# 在任务执行的时候 往mongodb中记录一条日志

def __call__(self, *args, **kwargs):
    """In celery task this function call the run method, here you can
    set some environment variable before the run of the task"""

    #Inizialize context managers    

    self.taskLogger = TaskLogger(args, kwargs)      #记录到Mongo
    self.taskLogger.__enter__()

    return self.run(*args, **kwargs)

def after_return(self, status, retval, task_id, args, kwargs, einfo):
    #exit point for context managers
    self.taskLogger.__exit__(status, retval, task_id, args, kwargs, einfo)
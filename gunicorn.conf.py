import multiprocessing
bind = "127.0.0.1:9005"
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 30

import ast
import re
import psutil


def process_iter_wrapper(name=None, pid=None, username=None):
    processes = list(psutil.process_iter())
    if name is not None:
        processes = filter(lambda x: (re.match(name, x.name())), processes)
    if username is not None:
        processes = filter(lambda x: (re.match(username, x.username())), processes)
    if pid is not None:
        try:
            pids = list(ast.literal_eval(pid))
            processes = filter(lambda x: (x.pid in pids), processes)
        except:
            try:
                if re.match(">=", pid):
                    pids = int(re.sub(">=", "", pid))
                    processes = filter(lambda x: (x.pid >= pids), processes)
                elif re.match("<=", pid):
                    pids = int(re.sub("<=", "", pid))
                    processes = filter(lambda x: (x.pid <= pids), processes)
                elif re.match(">", pid):
                    pids = int(re.sub(">", "", pid))
                    processes = filter(lambda x: (x.pid > pids), processes)
                elif re.match("<", pid):
                    pids = int(re.sub("<", "", pid))
                    processes = filter(lambda x: (x.pid < pids), processes)
                else:
                    pids = int(pid)
                    processes = filter(lambda x: (x.pid == pids), processes)
            except:
                print("pid is invalid")
    return processes


result = process_iter_wrapper(None, "[1,2,3]", "[a-z]")
result1 = process_iter_wrapper(None, "<4", "[a-z]")
result2 = process_iter_wrapper(None, "1", "[a-z]")
for r in result:
    print(r.username(), r.name(), r.pid, r.memory_percent())
print("****************************")
for r in result1:
    print(r.username(), r.name(), r.pid, r.memory_percent())
print("****************************")
for r in result2:
    print(r.username(), r.name(), r.pid, r.memory_percent())
print("****************************")

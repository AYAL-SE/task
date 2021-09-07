import ast
import re
import psutil


def process_iter_wrapper(name=None, pid=None, username=None):
    """

    :param name:
    :param pid:
    :param username:
    :return:
    """
    processes = list(psutil.process_iter())
    if name is not None:
        processes = filter(lambda x: (re.search(name, x.name())), processes)
    if username is not None:
        processes = filter(lambda x: (re.search(username, x.username())), processes)
    if pid is not None:
        try:
            pids = list(ast.literal_eval(pid))
            processes = filter(lambda x: (x.pid in pids), processes)
        except ValueError:
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
            except ValueError:
                print("pid is invalid")
    return processes


def print_result(results):
    """

    :param results:
    :return:
    """
    for process in results:
        try:
            print(process.username(), process.name(), process.pid, process.memory_percent())
        except psutil.NoSuchProcess:
            print("closed process")
    print("****************************")


#result = process_iter_wrapper(None, "[1,2,3]", "[a-z]")
#printResult(result)
#result1 = process_iter_wrapper(None, "<4", "[a-z]")
#printResult(result1)
#result2 = process_iter_wrapper(None, "1", "[a-z]")
#printResult(result2)
RESULT = process_iter_wrapper(None, None, 'a+')
print_result(RESULT)

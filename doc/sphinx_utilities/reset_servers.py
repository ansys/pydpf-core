#
def reset_servers(gallery_conf, fname, when):
    import gc

    import psutil

    from ansys.dpf.core import server

    gc.collect()
    server.shutdown_all_session_servers()

    proc_name = "Ans.Dpf.Grpc"
    nb_procs = 0
    for proc in psutil.process_iter():
        try:
            # check whether the process name matches
            if proc_name in proc.name():
                proc.kill()
                nb_procs += 1
        except psutil.NoSuchProcess:
            pass
    print(f"Counted {nb_procs} {proc_name} processes {when} example {fname}.")

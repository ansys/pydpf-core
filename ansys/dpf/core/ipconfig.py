import socket 

def get_local_ip():
    """
    heuristic for determining an ip address to connect to the grpc service
    :return: ip address in string form
    """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
        except socket.error:
            return '127.0.0.1'

        return s.getsockname()[0]

ip=get_local_ip()
port = 50052
environment = "windows"
configuration ="release"

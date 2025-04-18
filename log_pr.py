import re

def open_logfile(path: str) -> str:
    try:
        with open(path, 'r') as logs:
            text = logs.read()
            return text
    except FileNotFoundError as e:
        print(str(e))

def get_all_logs(file: str) -> list[tuple]:
    f""""The function takes a string as input and returns a list of tuples with the following elements:\n
        tuple[0] — The IP address of the client that sent the request to the server\n
        tuple[1] — The remote name of the user making the request\n
        tuple[2] — ID of the user making the request\n
        tuple[3] — Date of request\n
        tuple[4] — Request time\n
        tuple[5] — UTC time zone\n
        tuple[6] — Request type: (GET, POST, PUT, DELETE) that the server received\n
        tuple[7] — The API of the website the request pertains to\n
        tuple[8] — The protocol used to connect to the server and its version\n
        tuple[9] — The status code that the server returned for the request\n
        tuple[10] — The amount of data in bytes sent back to the client\n
        tuple[11] — Sources from which the user was directed to the current website (referrer)\n
        tuple[12] — User agent string (UA-string), contains information about the browser and host device\n
        tuple[13] — The response time it took for the server to serve the request\n
        """
    reg_ex = re.compile(r"(\b(?:\d{1,3}\.){3}\d{1,3}\b) (\w+|\W) (\w+|\W) "
                        r"\[(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\+\d+)] "
                        r"\"(GET|POST|PUT|DELETE) ([/\w+]+) ([\w/.]+)\" "
                        r"(\d+) (\d+) \"(.+)\" \"(.+)\" (\d+)"
                        )
    r_type = re.findall(reg_ex, file)
    return r_type

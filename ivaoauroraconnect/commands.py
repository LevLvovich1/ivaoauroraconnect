import socket
from tkinter.messagebox import showerror

HOST = "127.0.0.1"
PORT = 1130


class Error(Exception):
    pass


class Not_Provided(Exception):
    pass


def command(cmnd: str, points=None, s=None):
    """Custom commands."""
    if s != None:
        cmnd.replace("#", "")
        command = f"#{cmnd}\n"
        s.sendall(command.encode("ascii"))
        response = s.recv(1024)
        response_str = response.decode("ascii")
        response_str = response_str.strip()
        if response_str.startswith(f"#{cmnd};"):
            response_str = response_str[len(f"#{cmnd};") :]
        parts = response_str.split(";")
        values = parts[0:]
        values_list = [value.strip() for value in values]
        if points == None:
            return values_list
        if values_list[points] != "":
            return values_list[points]
        else:
            return ""
    else:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((HOST, PORT))
                cmnd.replace("#", "")
                command = f"#{cmnd}\n"
                s.sendall(command.encode("ascii"))
                response = s.recv(1024)
                response_str = response.decode("ascii")
                response_str = response_str.strip()
                if response_str.startswith(f"#{cmnd};"):
                    response_str = response_str[len(f"#{cmnd};") :]
                parts = response_str.split(";")
                values = parts[0:]
                values_list = [value.strip() for value in values]
                if points == None:
                    return values_list
                if values_list[points] != "":
                    return values_list[points]
                else:
                    return ""
            except ConnectionRefusedError as e:
                raise Error("Aurora not responding.")
            except Exception as e:
                raise Error(e)


def SELTFC() -> str or None:
    """Returns selected traffic."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#SELTFC\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#SELTFC;"):
                response_str = response_str[len(f"#SELTFC;") :]
            else:
                raise Error("Something went wrong.")
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            if values_list[0] != "":
                return values_list[0]
            else:
                return None
        except ConnectionRefusedError:
            raise Error(
                "Aurora not responding. Make sure Aurora allow 3rd party software."
            )
        except Exception as e:
            raise Error(e)


def TR() -> list or None:
    """Returns traffic in range."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#TR\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#TR;"):
                response_str = response_str[len(f"#TR;") :]
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            return values_list
        except ConnectionRefusedError:
            raise Error(
                "Aurora not responding. Make sure Aurora allow 3rd party software."
            )
        except Exception as e:
            raise Error(e)


def FP(cs: str, point: int = None):
    """Returns flightplan for acft."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#FP;{cs}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#FP;"):
                response_str = response_str[len(f"#FP;") :]
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            if point == None:
                return values_list
            if values_list[point] != "":
                return values_list[point]
            else:
                return ""
        except ConnectionRefusedError as e:
            raise Error("Aurora not responding.")
        except Exception as e:
            raise Error(e)


def FP_S(point: int = None):
    """Returns flightplan for selected acft."""
    if SELTFC() != None:
        cs = SELTFC()
    else:
        raise Error("No traffic selected.")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#FP;{cs}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#FP;"):
                response_str = response_str[len(f"#FP;") :]
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            if point == None:
                return values_list
            if values_list[point] != "":
                return values_list[point]
            else:
                return ""
        except ConnectionRefusedError as e:
            raise Error("Aurora not responding.")
        except Exception as e:
            raise Error(e)


def TRPOS(cs: str, point: int = None):
    """Returns position for acft."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#TRPOS;{cs}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#TRPOS;"):
                response_str = response_str[len(f"#TRPOS;") :]
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            if point == None:
                return values_list
            if values_list[point] != "":
                return values_list[point]
            else:
                return ""
        except ConnectionRefusedError as e:
            raise Error("Aurora not responding.")
        except Exception as e:
            raise Error(e)


def TRPOS_S(point: int = None):
    """Returns position for selected acft."""
    if SELTFC() != None:
        cs = SELTFC()
    else:
        raise Error("No traffic selected.")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#TRPOS;{cs}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#TRPOS;"):
                response_str = response_str[len(f"#TRPOS;") :]
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            if point == None:
                return values_list
            if values_list[point] != "":
                return values_list[point]
            else:
                return ""
        except ConnectionRefusedError as e:
            raise Error("Aurora not responding.")
        except Exception as e:
            raise Error(e)


def TRAS(cs: str):
    """Assume traffic."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#TRAS;{cs}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#TRAS;"):
                response_str = response_str[len(f"#TRAS;") :]
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]

            return
        except ConnectionRefusedError as e:
            raise Error("Aurora not responding.")
        except Exception as e:
            raise Error(e)


def TRAS_S():
    """Assume selected traffic."""
    if SELTFC() != None:
        cs = SELTFC()
    else:
        raise Error("No traffic selected.")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#TRAS;{cs}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#TRAS;"):
                response_str = response_str[len(f"#TRAS;") :]
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            return
        except ConnectionRefusedError as e:
            raise Error("Aurora not responding.")
        except Exception as e:
            raise Error(e)


def TRRE(cs: str):
    """Release traffic."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#TRRE;{cs}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#TRRE;"):
                response_str = response_str[len(f"#TRRE;") :]
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            return
        except ConnectionRefusedError as e:
            raise Error("Aurora not responding.")
        except Exception as e:
            raise Error(e)


def TRRE_S():
    """Release selected trafic."""
    if SELTFC() != None:
        cs = SELTFC()
    else:
        raise Error("No traffic selected.")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#TRRE;{cs}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#TRRE;"):
                response_str = response_str[len(f"#TRRE;") :]
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            return
        except ConnectionRefusedError as e:
            raise Error("Aurora not responding.")
        except Exception as e:
            raise Error(e)


def ZTR(cs: str):
    """Zoom traffic."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#ZTR;{cs}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#ZTR;"):
                response_str = response_str[len(f"#ZTR;") :]
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            return
        except ConnectionRefusedError as e:
            raise Error("Aurora not responding.")
        except Exception as e:
            raise Error(e)


def ZTR_S():
    """Zoom selected trafic."""
    if SELTFC() != None:
        cs = SELTFC()
    else:
        raise Error("No traffic selected.")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#ZTR;{cs}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#ZTR;"):
                response_str = response_str[len(f"#ZTR;") :]
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            return
        except ConnectionRefusedError as e:
            raise Error("Aurora not responding.")
        except Exception as e:
            raise Error(e)


def ZSTR(cs: str):
    """Zoom and select traffic."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#ZTR;{cs}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#ZTR;"):
                response_str = response_str[len(f"#ZTR;") :]
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            return
        except ConnectionRefusedError as e:
            raise Error("Aurora not responding.")
        except Exception as e:
            raise Error(e)


def LBWP(cs: str, wp: str):
    """Fill WP for traffic."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#ZTR;{cs};{wp}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#LBWP;"):
                response_str = response_str[len(f"#LBWP;") :]
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            return
        except ConnectionRefusedError as e:
            raise Error("Aurora not responding.")
        except Exception as e:
            raise Error(e)


def LBWP_S(wp: str):
    """Fill WP for selected trafic."""
    if SELTFC() != None:
        cs = SELTFC()
    else:
        raise Error("No traffic selected.")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#LBWP;{cs};{wp}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#LBWP;"):
                response_str = response_str[len(f"#LBWP;") :]
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            return
        except ConnectionRefusedError as e:
            raise Error("Aurora not responding.")
        except Exception as e:
            raise Error(e)


def LBALT(cs: str, alt: str):
    """Fill ALT for traffic."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#LBALT;{cs};{alt}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#LBALT;"):
                response_str = response_str[len(f"#LBALT;") :]
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            return
        except ConnectionRefusedError as e:
            raise Error("Aurora not responding.")
        except Exception as e:
            raise Error(e)


def LBALT_S(alt: str):
    """Fill ALT for selected trafic."""
    if SELTFC() != None:
        cs = SELTFC()
    else:
        raise Error("No traffic selected.")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#LBALT;{cs};{alt}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#LBALT;"):
                response_str = response_str[len(f"#LBALT;") :]
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            return
        except ConnectionRefusedError as e:
            raise Error("Aurora not responding.")
        except Exception as e:
            raise Error(e)


def LBSPD(cs: str, spd: str):
    """Fill SPD for traffic."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#LBALT;{cs};{spd}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#LBSPD;"):
                response_str = response_str[len(f"#LBSPD;") :]
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            return
        except ConnectionRefusedError as e:
            raise Error("Aurora not responding.")
        except Exception as e:
            raise Error(e)


def LBSPD_S(spd: str):
    """Fill SPD for selected trafic."""
    if SELTFC() != None:
        cs = SELTFC()
    else:
        raise Error("No traffic selected.")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#LBALT;{cs};{spd}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#LBALT;"):
                response_str = response_str[len(f"#LBALT;") :]
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]

            return
        except ConnectionRefusedError as e:
            raise Error("Aurora not responding.")
        except Exception as e:
            raise Error(e)


def LBSQK(cs: str, sqk: str):
    """Fill SPD for traffic."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#LBSQK;{cs};{sqk}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#LBSQK;"):
                response_str = response_str[len(f"#LBSQK;") :]
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            return
        except ConnectionRefusedError as e:
            raise Error("Aurora not responding.")
        except Exception as e:
            raise Error(e)


def LBSQK_S(sqk: str):
    """Fill SPD for selected trafic."""
    if SELTFC() != None:
        cs = SELTFC()
    else:
        raise Error("No traffic selected.")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#LBSQK;{cs};{sqk}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#LBSQK;"):
                response_str = response_str[len(f"#LBSQK;") :]
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]

            return
        except ConnectionRefusedError as e:
            raise Error("Aurora not responding.")
        except Exception as e:
            raise Error(e)


def TRSQK(cs: str):
    """Returns generated SQK for traffic."""
    raise Not_Provided("Now TRSQK not provided.")


def TRSQK_S():
    """Returns generated SQK for selected traffic."""
    raise Not_Provided("Now TRSQK not provided.")


def ATC() -> list or None:
    """Returns ATC in range."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#ATC\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#ATC;"):
                response_str = response_str[len(f"#ATC;") :]
            else:
                raise Error("Something went wrong.")
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            return values_list
        except ConnectionRefusedError:
            raise Error(
                "Aurora not responding. Make sure Aurora allow 3rd party software."
            )
        except Exception as e:
            raise Error(e)


def ATCT() -> str or None:
    """Returns ATC in transfer list."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#ATCT\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#ATCT;"):
                response_str = response_str[len(f"#ATCT;") :]
            else:
                raise Error("Something went wrong.")
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            return values_list
        except ConnectionRefusedError:
            raise Error(
                "Aurora not responding. Make sure Aurora allow 3rd party software."
            )
        except Exception as e:
            raise Error(e)


def ATCTA(atc: str):
    """Add ATC to transfer list."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#ATCTA;{atc}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#ATCTA;"):
                response_str = response_str[len(f"#ATCTA;") :]
            else:
                raise Error("Something went wrong.")
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            return
        except ConnectionRefusedError:
            raise Error(
                "Aurora not responding. Make sure Aurora allow 3rd party software."
            )
        except Exception as e:
            raise Error(e)


def ATCTR(atc: str):
    """Remove ATC from transfer list."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#ATCTR;{atc}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#ATCTR;"):
                response_str = response_str[len(f"#ATCTR;") :]
            else:
                raise Error("Something went wrong.")
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            return
        except ConnectionRefusedError:
            raise Error(
                "Aurora not responding. Make sure Aurora allow 3rd party software."
            )
        except Exception as e:
            raise Error(e)


def MSGFR(cs: str, text: str):
    """Send message to primary frequency."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#MSGFR;{cs};{text}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#MSGFR;"):
                response_str = response_str[len(f"#MSGFR;") :]
            else:
                raise Error("Something went wrong.")
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            return
        except ConnectionRefusedError:
            raise Error(
                "Aurora not responding. Make sure Aurora allow 3rd party software."
            )
        except Exception as e:
            raise Error(e)


def MSGPM(cs: str, text: str):
    """Send PM."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#MSGPM;{cs};{text}\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#MSGPM;"):
                response_str = response_str[len(f"#MSGPM;") :]
            else:
                raise Error("Something went wrong.")
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            return
        except ConnectionRefusedError:
            raise Error(
                "Aurora not responding. Make sure Aurora allow 3rd party software."
            )
        except Exception as e:
            raise Error(e)


def TRPATHA():
    """???"""
    raise Not_Provided("Now TRPATHA not provided.")


def TRPATHL():
    """???"""
    raise Not_Provided("Now TRPATHL not provided.")


def METAR_ALT() -> str or None:
    """Returns metar from alternative source."""
    raise Not_Provided("Now METAR_ALT not provided.")


def METAR() -> str or None:
    """Returns metar for ARPT."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            command = f"#METAR\n"
            s.sendall(command.encode("ascii"))
            response = s.recv(1024)
            response_str = response.decode("ascii")
            response_str = response_str.strip()
            if response_str.startswith(f"#METAR;"):
                response_str = response_str[len(f"#METAR;") :]
            else:
                raise Error("Something went wrong.")
            parts = response_str.split(";")
            values = parts[0:]
            values_list = [value.strip() for value in values]
            if values_list[0] != "":
                return values_list[0]
            else:
                return None
        except ConnectionRefusedError:
            raise Error(
                "Aurora not responding. Make sure Aurora allow 3rd party software."
            )
        except Exception as e:
            raise Error(e)


# def decrypt_trpos(trpos: list):
#     print("Heading", trpos[0])
#     print("Track", trpos[1])
#     print("Altitude", trpos[2])
#     print("Speed", trpos[3])
#     print("Latitude", trpos[4])
#     print("Longitude", trpos[5])
#     print("SSR set", trpos[6])
#     print("SSR label", trpos[7])
#     print("WP label", trpos[8])
#     print("ALT label", trpos[9])
#     print("SPD label", trpos[10])
#     print("Assumed station", trpos[11])
#     print("Next station", trpos[12])
#     print("On ground", trpos[13])
#     print("Is selected", trpos[14])
#     print("Was selected", trpos[15])
#     print("Current gate", trpos[16])
#     print("Voice", trpos[17])

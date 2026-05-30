import socket
from tkinter.messagebox import showerror
from typing import Literal
from warnings import deprecated

HOST = "127.0.0.1"
PORT = 1130


class AuroraNotRespondingError(Exception):
    def __init__(self):
        super().__init__(
            "Aurora not responding. Make sure Aurora allow 3rd party software in settings."
        )


@deprecated("")
class Error(Exception):
    pass


class Connection:
    def __init__(self):
        try:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__socket.connect(("127.0.0.1", 1130))
        except ConnectionRefusedError:
            raise AuroraNotRespondingError

    def __enter__(self):
        return self

    def close(self):
        self.__socket.shutdown(socket.SHUT_RDWR)
        self.__socket.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def _command(self, command: str):
        command = f"#{command}\n" if not command.startswith("#") else command
        self.__socket.sendall(command.encode("ascii"))
        response = self.__socket.recv(1024)
        response_str = response.decode("ascii")
        response_str = response_str.strip()
        if response_str.startswith(command):
            response_str = response_str[len(command) :]
        parts = response_str.split(";")
        values = parts[0:]
        values_list = [value.strip() for value in values]
        return values_list

    def _selected_aircraft(self):
        return self._command("SELTFC")

    def tr(self):
        return self._command("TR")

    def fp(self, callsign):
        return self._command(f"FP;{callsign}")

    def fp_s(self):
        callsign = self._selected_aircraft()
        self.fp(callsign)

    def seltfc(self):
        return self._command("SELTFC")

    def trpos(self, cs):
        return self._command(f"TRPOS;{cs}")

    def trpos_s(self):
        cs = self._selected_aircraft()
        return self.trpos(cs)

    def tras(self, cs):
        return self._command(f"TRAS;{cs}")

    def tras_s(self):
        cs = self._selected_aircraft()
        return self.tras(cs)

    def trre(self, cs):
        return self._command(f"TRRE;{cs}")

    def trre_s(self):
        cs = self._selected_aircraft()
        return self.trre(cs)

    def ztr(self, cs):
        return self._command(f"ZTR;{cs}")

    def ztr_s(self):
        cs = self._selected_aircraft()
        return self.ztr(cs)

    def zstr(self, cs):
        return self._command(f"ZSTR;{cs}")

    def lbwp(self, cs, wp):
        return self._command(f"LBWP;{cs};{wp}")

    def lbwp_s(self, wp):
        cs = self._selected_aircraft()
        return self.lbwp(cs, wp)

    def lbalt(self, cs, alt):
        return self._command(f"LBALT;{cs};{alt}")

    def lbalt_s(self, alt):
        cs = self._selected_aircraft()
        return self.lbalt(cs, alt)

    def lbspd(self, cs, spd):
        return self._command(f"LBSPD;{cs};{spd}")

    def lbspd_s(self, spd):
        cs = self._selected_aircraft()
        return self.lbspd(cs, spd)

    def lbsqk(self, cs, sqk):
        return self._command(f"LBSQK;{cs};{sqk}")

    def lbsqk_s(self, sqk):
        cs = self._selected_aircraft()
        return self.lbsqk(cs, sqk)

    def trsqk(self, cs):
        return self._command(f"TRSQK;{cs}")

    def trsqk_s(self):
        cs = self._selected_aircraft()
        return self.trsqk(cs)

    def atc(self):
        return self._command("ATC")

    def atct(self):
        return self._command("ATCT")

    def atcta(self, atc):
        return self._command(f"ATCTA;{atc}")

    def atctr(self, atc):
        return self._command(f"ATCTR;{atc}")

    def msgfr(self, cs, text):
        return self._command(f"MSGFR;{cs};{text}")

    def msgpm(self, cs, text):
        return self._command(f"MSGPM;{cs};{text}")

    def trpathl(self):
        return self._command("TRPATHL")

    def metar(self, icao):
        return self._command(f"METAR;{icao}")

    def bay(self):
        return self._command("BAY")

    def atis(self):
        return self._command("ATIS")

    def ctrl(self):
        return self._command("CTRL")

    def ctrlrwy(self):
        return self._command("CTRLRWY")

    def conn(self):
        return self._command("CONN")

    def cto(self, navaid):
        return self._command(f"CTO;{navaid}")

    def zto(self, zoom):
        return self._command(f"ZTO;{zoom}")

    def lbgte(self, cs, gate):
        return self._command(f"LBGTE;{cs};{gate}")

    def lbgte_s(self, gate):
        cs = self._selected_aircraft()
        return self.lbgte(cs, gate)

    def intercomcall(self, cs):
        return self._command(f"INTERCOMCALL;{cs}")

    def intercomanswer(self):
        return self._command("INTERCOMANSWER")

    def intercomreject(self):
        return self._command("INTERCOMREJECT")

    def intercomphonestatus(self):
        return self._command("INTERCOMPHONESTATUS")

    def intercomcallstatus(self):
        return self._command("INTERCOMCALLSTATUS")


@deprecated("Use Connection._command")
def command(cmnd: str, points=None, *args):
    try:
        with Connection() as conn:
            values_list = conn._command(cmnd)
            if points == None:
                return values_list
            if values_list[points] != "":
                return values_list[points]
            else:
                return ""
    except AuroraNotRespondingError:
        raise Error

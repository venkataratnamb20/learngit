#!/usr/bin/env python
import os

from pysim import run_shell

def run_ngspice(netlist: str|None = None, 
                filename: os.PathLike|None = None):
    if netlist is not None:
        cmd = """echo "$netlist" | ngspice -s"""
    if filename is not None:
        cmd = f"ngspice -b {filename}"
    result = run_shell(cmd)
    return result


if __name__ == "__main__":
    from pathlib import Path
    data_path = Path('./.data')
    data_path.mkdir(parents=True, exist_ok=True)

    netlist = """
    .TITLE resdiv
    R1 vin vout 10K
    R2 vout 0 10K
    * V1 vin 0 5
    VIN vin 0 PULSE(0 5 2NS 2NS 2NS 50NS 100NS 50)
    * .OP
    .TRAN 100p 400n

    .CONTROL
    save all;
    set filetype=ascii;
    set wr_singlescale            ; for wrdata: write the scale only once
    set wr_vecnames               ; for wrdata: write the vector names
    option numdgt = 3             ; for wrdata: 3 digits after decimal point
    tran 100p 400n;
    run;
    wrdata ./.data/resdiv_tran.csv all;
    rusage;
    .ENDC
    .END

    """
    netlist = netlist.replace("    ","")
    print(run_ngspice(netlist=netlist))
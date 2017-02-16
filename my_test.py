import my_debugger
from my_debugger_defines import *
debugger = my_debugger.debugger()
#debugger.load("C:\\WINDOWS\\system32\\calc.exe")
pid = raw_input("Enter the PID of the process to attach to: ")
debugger.attach(int(pid))
printf_address = debugger.func_resolve("msvcrt.dll","printf")
print "[*] Address of printf: 0x%08x" % printf_address
#debugger.bp_set(printf_address)
#debugger.bp_set_hw(printf_address,1,HW_EXECUTE)
debugger.bp_set_mem(printf_address,1)
debugger.run()
debugger.detach()

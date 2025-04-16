import gdb

class FindEntry(gdb.Command):
    """Find and display the ELF entry point of the loaded binary."""

    def __init__(self):
        super().__init__("find_entry", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        try:
            output = gdb.execute("info files", to_string=True)
            for line in output.splitlines():
                if "Entry point" in line:
                    print("[+] " + line.strip())
                    return
            print("[-] Entry point not found.")
        except gdb.error as e:
            print(f"[-] GDB Error: {e}")

FindEntry()

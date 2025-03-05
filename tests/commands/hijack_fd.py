from tests.remote import RemoteEnumTestGeneric

class HijackFdCommand(RemoteEnumTestGeneric):
    """Test for the hijack-fd command"""
    
    cmd = "hijack-fd"

    def test_cmd_run(self):
        """Test if the hijack-fd command runs without crashing"""
        gdb = self.target()
        res = gdb.execute(f"{self.cmd} 1 /dev/null", to_string=True)
        assert "Success" in res or "Redirected" in res, f"Unexpected output: {res}"

    def test_invalid_fd(self):
        """Test hijack-fd with an invalid file descriptor"""
        gdb = self.target()
        res = gdb.execute(f"{self.cmd} 99999 /dev/null", to_string=True)
        assert "invalid file descriptor" in res or "Error" in res, f"Unexpected output: {res}"

    def test_redirect_stdin(self):
        """Test hijack-fd redirecting STDIN"""
        gdb = self.target()
        res = gdb.execute(f"{self.cmd} 0 localhost:8888", to_string=True)
        assert "Redirected" in res or "Success" in res, f"Unexpected output: {res}"

    def test_nonexistent_file(self):
        """Test hijack-fd with a non-existent file"""
        gdb = self.target()
        res = gdb.execute(f"{self.cmd} 1 /this/does/not/exist", to_string=True)
        assert "no such file" in res or "Error" in res, f"Unexpected output: {res}"


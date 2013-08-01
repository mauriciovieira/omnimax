import os
import tempfile
import unittest
from omnimax.execute import execute, execute_file


class ExecuteTest(unittest.TestCase):

    def test_execute(self):
        msg = 'Hello, World!'
        result = execute('cat', msg)
        self.assertEquals(result, msg)

    def test_execute_file(self):
        script = """
        #!/bin/bash
        echo 'Hello, Max!'
        """
        scriptfile = tempfile.NamedTemporaryFile(suffix=".tmp", delete=False)
        scriptfile.write(script)
        scriptfile.flush()
        scriptfile.close()
        # Wrapper works around the fact /tmp may not allow execution
        result = execute_file(scriptfile.name, wrapper='bash')
        os.unlink(scriptfile.name)
        self.assertEquals(result, "Hello, Max!\n\n")

if __name__ == "__main__":  # pragma: no cover
    unittest.main()

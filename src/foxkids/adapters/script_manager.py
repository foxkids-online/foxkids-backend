import os
import stat

from foxkids.settings import settings


class ScriptManager:

    file_stream = settings.FILE_STREAM

    def write_stream_script(self, series: list[str]):
        with open(self.file_stream, "w+") as f:
            f.write("#!/bin/bash\n")
            f.writelines(series)
        st = os.stat(self.file_stream)
        os.chmod(self.file_stream, st.st_mode | stat.S_IEXEC)

    def get_stream_script(self):
        with open(self.file_stream, "r") as f:
            return f.read()

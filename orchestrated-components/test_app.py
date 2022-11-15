import os
import pytest
import time


from lightning_app.testing.testing import run_app_in_cloud


@pytest.mark.cloud
@pytest.mark.timeout(40)
def test_run_app():
    with run_app_in_cloud(os.path.dirname(__file__)) as (
        _,
        _,
        fetch_logs,
        _,
    ):
        # 6: Validate the logs.
        has_logs = False
        while not has_logs:
            for log in fetch_logs():
                if "['BENCHMARK 4 DONE']" in log:
                    has_logs = True
            time.sleep(0.1)

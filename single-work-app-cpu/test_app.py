import os
import pytest
import time


from lightning.app.testing.testing import run_app_in_cloud


APP_TIMEOUT_SECONDS = 30


@pytest.mark.cloud
@pytest.mark.retry(retries=3, delay=5)
def test_run_app():
    with run_app_in_cloud(os.path.dirname(__file__)) as (
        _,
        _,
        fetch_logs,
        _,
    ):
        start_time = time.time()
        has_logs = False
        while not has_logs:
            assert time.time() - start_time < APP_TIMEOUT_SECONDS
            for log in fetch_logs():
                if "['BENCHMARK 1 COMPLETE']" in log:
                    has_logs = True
            time.sleep(0.1)

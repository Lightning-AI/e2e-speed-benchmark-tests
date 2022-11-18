import logging
import os
import pytest
import time


from lightning.app.testing.testing import run_app_in_cloud


APP_TIMEOUT_SECONDS = 100

logger = logging.getLogger(__name__)


@pytest.mark.cloud
@pytest.mark.flaky(retries=3, delay=5)
def test_run_app():
    with run_app_in_cloud(os.path.dirname(__file__)) as (
        _,
        _,
        fetch_logs,
        _,
    ):
        start_time = None
        has_logs = False
        while not has_logs:
            if start_time is not None:
                assert time.time() - start_time < APP_TIMEOUT_SECONDS
            for log in fetch_logs():
                if "PRINTING LOGS" in log:
                    if start_time is None:
                        logger.info("recieved log line from app running in cloud")
                        start_time = time.time()
                if "BENCHMARK DONE" in log:
                    logger.info(f"benchmark has completed in {time.time() - start_time} seconds")
                    has_logs = True
            time.sleep(0.1)

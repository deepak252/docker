import asyncio
import time
from typing import Dict
import httpx

from app.models import ApiData, WrkResult


class WrkloadService:

    async def wrk(
        self,
        api_data: ApiData,
        connections: int,
        duration: int
    ) -> WrkResult:

        success_codes: Dict[int, int] = {}
        failure_codes: Dict[int, int] = {}

        total_hits = 0
        failure_hits = 0

        start = time.time()

        lock = asyncio.Lock()
        stop_time = start + duration

        async with httpx.AsyncClient(timeout=1.0, verify=False) as client:

            async def worker():
                nonlocal total_hits, failure_hits

                local_total = 0
                local_failed = 0

                while time.time() < stop_time:
                    try:
                        response = await client.get(api_data.url)

                        status_code = response.status_code

                        async with lock:
                            if status_code <= 299:
                                success_codes[status_code] = success_codes.get(status_code, 0) + 1
                            else:
                                failure_codes[status_code] = failure_codes.get(status_code, 0) + 1

                        local_total += 1

                    except Exception as e:
                        print(e)
                        local_total += 1
                        local_failed += 1

                async with lock:
                    total_hits += local_total
                    failure_hits += local_failed

            tasks = [asyncio.create_task(worker()) for _ in range(connections)]

            await asyncio.gather(*tasks)

        return WrkResult(
            url=api_data.url,
            method=api_data.method,
            connections=connections,
            time_taken=f"{time.time() - start:.3f}s",
            total_hits=total_hits,
            success_hits=total_hits - failure_hits,
            failure_hits=failure_hits,
            success_messages=success_codes,
            failure_messages=failure_codes,
        )
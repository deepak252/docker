import asyncio
import httpx
import time

URL = "http://localhost:8084/api/v1/companies/produce?count=10000"
TOTAL_REQUESTS = 8

async def hit_api(client, idx):
    try:
        resp = await client.post(URL)

        if resp.status_code == 200:
            print(f"[{idx}] ✅ Status: {resp.status_code}")
            print(f"[{idx}] ✅ Response Body: {resp.text}\n")
            return True
        else:
            print(
                f"[{idx}] ❌ Failed | Status: {resp.status_code} | Body: {resp.text}"
            )
            return False

    except httpx.RequestError as e:
        print(f"[{idx}] ❌ Request error: {str(e)}")
        return False

    except Exception as e:
        print(f"[{idx}] ❌ Unexpected error: {str(e)}")
        return False


async def main():
    start_time = time.perf_counter()

    async with httpx.AsyncClient(timeout=300) as client:
        tasks = [hit_api(client, i) for i in range(1, TOTAL_REQUESTS + 1)]
        results = await asyncio.gather(*tasks)

    elapsed_time = time.perf_counter() - start_time

    success = sum(results)
    failed = TOTAL_REQUESTS - success

    print("\n====== SUMMARY ======")
    print(f"Total Requests : {TOTAL_REQUESTS}")
    print(f"Successful     : {success}")
    print(f"Failed         : {failed}")
    print(f"Time Taken     : {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())

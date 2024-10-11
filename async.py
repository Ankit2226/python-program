import asyncio
delay=0.5

async def fetch_data(delay):
    await asyncio.sleep(delay)
    return f"data after {delay} seconds"
async def main():
     tasks = [fetch_data(i) for i in range (1,6)]    

async def feture_data(id):
     delay = random.uniform(0.5)    
     
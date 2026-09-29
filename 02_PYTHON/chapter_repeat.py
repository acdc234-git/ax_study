import httpx
import asyncio

todo = [1,2,3,4,5]

async def fetch_todo_by_id(num):
    async with httpx.AsyncClient() as client:
        url = f"https://jsonplaceholder.typicode.com/posts/{num}"

        res = await client.get(url)
        result = res.json()

        return result['id'], result['title']

async def main():
    todo_list = [ fetch_todo_by_id(i) for i in todo]

    result = await asyncio.gather(*todo_list)
    print(result)    

asyncio.run(main())
import math

async def get_triday(day):
    triday = math.ceil(day / 3)
    return triday

async def get_days_from_triday(triday):
    triday *= 3
    days = [triday - 2, triday - 1, triday]
    return days

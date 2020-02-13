import asyncio
import random
import time
import ga4gh.refget.tester.config.constants as c
from ga4gh.refget.tester.requester import Requester

async def single_request(route_name):
    # await asyncio.sleep(random.randint(0, 3))

    url_template = c.TEMPLATES_DICT[route_name]
    seqid = None
    params = {}
    headers = {}

    # get sequence id
    if route_name == "sequence" or route_name == "metadata":
        seqid = c.SEQIDS[random.randint(0, len(c.SEQIDS) - 1)]
    
    # randomly set subsequence parameters for "sequence" endpoint
    if route_name == "sequence":
        param_type = c.PARAM_TYPES[random.randint(0, len(c.PARAM_TYPES) -1)]

        nums = []
        if param_type == "start-end":
            nums = random.sample(range(0, c.SEQLENGTHS[seqid]), 2)
            sorted_nums = sorted(nums)
            params["start"] = sorted_nums[0]
            params["end"] = sorted_nums[1]

        elif param_type == "range":
            nums = random.sample(range(0, c.SEQLENGTHS[seqid] -1), 2)
            sorted_nums = sorted(nums)
            headers["Range"] = "bytes=%d-%d" % (sorted_nums[0], sorted_nums[1])

    # print("ready to request: " + seqid)
    r = Requester(url_template, seqid, params, headers)
    response = r.make_request()
    return response

async def many_requests(route_name, n_requests):
    for i in range(0, n_requests):
        print("%s\t%s" % (route_name, i))
        await asyncio.create_task(single_request(route_name))

async def sequence_requests(n_requests):
    await asyncio.create_task(many_requests("sequence", n_requests))

async def metadata_requests(n_requests):
    await asyncio.create_task(many_requests("metadata", n_requests))

async def serviceinfo_requests(n_requests):
    await asyncio.create_task(many_requests("service-info", n_requests))

async def run():

    n = 1000
    sequence_task = asyncio.create_task(sequence_requests(n))
    metadata_task = asyncio.create_task(metadata_requests(n))
    serviceinfo_task = asyncio.create_task(serviceinfo_requests(n))
    
    await sequence_task
    await metadata_task
    await serviceinfo_task
    print("DONE")

def main():
    asyncio.run(run())


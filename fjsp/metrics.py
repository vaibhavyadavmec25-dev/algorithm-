from collections import defaultdict

def metrics(instance,schedule):
    makespan=max((x["completion_time"] for x in schedule),default=0)
    busy=defaultdict(float)
    for x in schedule: busy[x["machine_id"]]+=x["completion_time"]-x["start_time"]
    util={m:(busy[m]/makespan if makespan else 0) for m in range(instance.number_of_machines)}
    return {"makespan":makespan,"machine_utilization":util,
            "total_busy_time":sum(busy.values())}

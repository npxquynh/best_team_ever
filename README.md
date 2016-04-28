The solution for the problem in Qualification Round for HashCode 2016. The problem description can be read [here](https://hashcode.withgoogle.com/2016/tasks/hashcode2016_qualification_task.pdf)

The problem is finding the optimal schedule for drones, with the constraint on the weight that a single drone can carry, within the limited time period. We want drones to deliver as many requests as possible, and finish all the requests the sooner the better.

### Solution
My solution evolves from the simplest solution to a little bit more complicated one:

Naive solution:
- A single drone delivers a single product to a single location. If destination D requires 10 items, then the drone would fly back-and-forth 10 times.
- A single drone runs for the whole time of the simulation, and then the next drone will be chosen to continue the task.
- If there are multiple warehouses, then drone always pick the first warehouse in the list. If the first warehouse does not have needed item, then drones will check with the second warehouse.

Improved solution:
- A single drone fly to one warehouse, and pick as many as items that it can carry, and then deliver it.
- Making drone aware of the needed items in the warehouse closest to its current location, and choose the nearest warehouse with available items. This minimize the flying time for drones.

### Results
Ranked 2th for a hub in Trentino area, Italy (of 3 teams)
Ranked 2th fora hub in King's College London (of 9 teams)

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        one, svn, trty = costs
        #0: 0 as placeholder; 1 indexed so first_day = idx 1
        #ex. ld = 5 fd = 2 then [0, 1, 2, 3, 4] so idx = day - fd + 1
        first_day = days[0]
        last_day = days[-1]
        last_idx = last_day - first_day + 1
        print(last_idx + 1)
        #min cost of traveling all the chosen dates up to and including dates[idx]
        dates = [0 if day == 0 else float('inf') for day in range(last_idx + 1)]

        trav = set([day - first_day + 1 for day in days])

        for date in range(1, last_idx + 1):
            #min cost covering up to today should be
            d_cost, m_cost, w_cost = [float('inf'), float('inf'), float('inf')]
            #1. cost for today + cost up to yesterday
            #print(date, day)
            if date not in trav:
                dates[date] = dates[date - 1]
                continue
            else: 
                d_cost = dates[max(0, date - 1)] + one
                w_cost = dates[max(0, date - 7)] + svn
                m_cost = dates[max(0, date - 30)] + trty
                #print(date, m_cost, w_cost, d_cost)
                
                dates[date] = min(m_cost, w_cost, d_cost, dates[date])
                #print(date, dates)

            #prev = curr
            #print(day, prev)

        return dates[-1]

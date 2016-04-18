#!/usr/bin/env python3
import os
from _decimal import Decimal

import time

from supplychainpy import simulate
from supplychainpy import model_inventory

__author__ = 'kevin'


def main():
    start_time = time.time()

    orders_analysis = model_inventory.analyse_orders_abcxyz_from_file(file_path="data2.csv", z_value=Decimal(1.28),
                                                                      reorder_cost=Decimal(5000), file_type="csv",
                                                                      length=12)

    print(orders_analysis.orders)

    sim = simulate.run_monte_carlo(orders_analysis=orders_analysis.orders, runs=1, period_length=12)

    sim_window = simulate.summarize_window(simulation_frame=sim, period_length=12)

    sim_frame = simulate.summarise_frame(sim_window)

   # optimised = simulate.optimise_service_level(service_level=90.0, frame_summary=sim_frame,
   #                                             orders_analysis=orders_analysis.orders, runs=1,
   #                                             percentage_increase=3.0)

    for s in sim_frame:
        print(s)

    end_time = time.time()
    elapsed = end_time - start_time
    print(elapsed)


if __name__ == '__main__':
    main()

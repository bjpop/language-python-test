#!/usr/bin/env python

import sched
import time
import unittest
from test import support


class TestCase(unittest.TestCase):

    def test_enter(self):
        l = []
        fun = lambda x: l.append(x)
        scheduler = sched.scheduler(time.time, time.sleep)
        for x in [0.5, 0.4, 0.3, 0.2, 0.1]:
            z = scheduler.enter(x, 1, fun, (x,))
        scheduler.run()
        self.assertEqual(l, [0.1, 0.2, 0.3, 0.4, 0.5])

    def test_enterabs(self):
        l = []
        fun = lambda x: l.append(x)
        scheduler = sched.scheduler(time.time, time.sleep)
        for x in [0.05, 0.04, 0.03, 0.02, 0.01]:
            z = scheduler.enterabs(x, 1, fun, (x,))
        scheduler.run()
        self.assertEqual(l, [0.01, 0.02, 0.03, 0.04, 0.05])

    def test_priority(self):
        l = []
        fun = lambda x: l.append(x)
        scheduler = sched.scheduler(time.time, time.sleep)
        for priority in [1, 2, 3, 4, 5]:
            z = scheduler.enterabs(0.01, priority, fun, (priority,))
        scheduler.run()
        self.assertEqual(l, [1, 2, 3, 4, 5])

    def test_cancel(self):
        l = []
        fun = lambda x: l.append(x)
        scheduler = sched.scheduler(time.time, time.sleep)
        now = time.time()
        event1 = scheduler.enterabs(now + 0.01, 1, fun, (0.01,))
        event2 = scheduler.enterabs(now + 0.02, 1, fun, (0.02,))
        event3 = scheduler.enterabs(now + 0.03, 1, fun, (0.03,))
        event4 = scheduler.enterabs(now + 0.04, 1, fun, (0.04,))
        event5 = scheduler.enterabs(now + 0.05, 1, fun, (0.05,))
        scheduler.cancel(event1)
        scheduler.cancel(event5)
        scheduler.run()
        self.assertEqual(l, [0.02, 0.03, 0.04])

    def test_empty(self):
        l = []
        fun = lambda x: l.append(x)
        scheduler = sched.scheduler(time.time, time.sleep)
        self.assertTrue(scheduler.empty())
        for x in [0.05, 0.04, 0.03, 0.02, 0.01]:
            z = scheduler.enterabs(x, 1, fun, (x,))
        self.assertFalse(scheduler.empty())
        scheduler.run()
        self.assertTrue(scheduler.empty())

    def test_queue(self):
        l = []
        fun = lambda x: l.append(x)
        scheduler = sched.scheduler(time.time, time.sleep)
        now = time.time()
        e5 = scheduler.enterabs(now + 0.05, 1, fun)
        e1 = scheduler.enterabs(now + 0.01, 1, fun)
        e2 = scheduler.enterabs(now + 0.02, 1, fun)
        e4 = scheduler.enterabs(now + 0.04, 1, fun)
        e3 = scheduler.enterabs(now + 0.03, 1, fun)
        # queue property is supposed to return an order list of
        # upcoming events
        self.assertEqual(list(scheduler.queue), [e1, e2, e3, e4, e5])

    def test_args_kwargs(self):
        flag = []

        def fun(*a, **b):
            flag.append(None)
            self.assertEqual(a, (1,2,3))
            self.assertEqual(b, {"foo":1})

        scheduler = sched.scheduler(time.time, time.sleep)
        z = scheduler.enterabs(0.01, 1, fun, argument=(1,2,3), kwargs={"foo":1})
        scheduler.run()
        self.assertEqual(flag, [None])

    def test_run_non_blocking(self):
        l = []
        fun = lambda x: l.append(x)
        scheduler = sched.scheduler(time.time, time.sleep)
        for x in [10, 9, 8, 7, 6]:
            scheduler.enter(x, 1, fun, (x,))
        scheduler.run(blocking=False)
        self.assertEqual(l, [])


def test_main():
    support.run_unittest(TestCase)

if __name__ == "__main__":
    test_main()

# clarity
# what levels of employees in the call center? operator, supervisor, director
# can we assume operators always the the inital calls? y
# if no available operator or operator can't handle the call, call go to supervisor
# if no supervisor, go to director
# can we assume director can handle all calls? y

# what happens if nobody can answer the call ? it gets queued
# is there VIP calls that put to the front of the line? NO
# can we assume all inputs valid or do we have to validate> valid

from enum import Enum
from collections import deque
from abc import ABC, ABCMeta, abstractmethod


class Rank(Enum):
    OPERATOR = 0
    SUPERVISOR = 1
    DIRECTOR = 2


class Employee(ABC):
    def __init__(self, id, name, rank, call_center):
        self.id = id
        self.name = name
        self.rank = rank
        self.call = None
        self.call_center = call_center

    def take_call(self, call):
        self.call = call
        self.call.employee = self
        self.call.state = CallState.IN_PROGRESS

    def complete_call(self):
        self.call.state = CallState.COMPLETE  # change call state
        call = self.call
        self.call_center.notify_call_completed(call) # notify center free
        self.call = None  # free people

    @abstractmethod
    def escalate_call(self):
        pass

    def _escalate_call(self):
        self.call.state = CallState.Ready
        self.call_center.notify_call_escalated(self.call)  # notify
        self.call = None # free

class Operator(Employee):
    def __init__(self, id, name):
        super(Operator, self).__init__(id, name, Rank.OPERATOR)

    def escalate_call(self):
        self.call.level = Rank.SUPERVISOR
        self._escalate_call()

class Supervisor(Employee):
    def __init__(self, id, name):
        super(Supervisor, self).__init__(id, name, Rank.SUPERVISOR)

    def escalate_call(self):
        self.call.level = Rank.DIRECTOR
        self._escalate_call()

class Director(Employee):
    def __init__(self, id, name):
        super(Director, self).__init__(id, name, Rank.DIRECTOR)

    def escalate_call(self):
        raise NotImplemented("Director can't escalate.")


class CallState(Enum):
    READY = 0
    IN_PROGRESS = 1
    COMPLETE = 2


class Call:
    def __init__(self, rank):
        self.state = CallState.READY
        self.rank = rank
        self.employee = None

# a call center needs to: dispatch incoming call, keep queued call, (be notified when call escalated or
# completed.) its knows all employees and a wait list of calls
class CallCenter:
    def __init__(self, operators, supervisors, directors):
        self.operators = operators
        self.supervisors = supervisors
        self.directors = directors
        self.queued_calls = [deque()] * 3

    def dispatch_call(self, call):
        """
        dispatch call to its corresponding ranking staff,
        if full, put into queue
        :param call:
        :return:
        """
        if call.rank not in (Rank.DIRECTOR, Rank.SUPERVISOR, Rank.OPERATOR):
            raise ValueError("Invalid call with rank: {}". format(str(call.rank)))
        e = None
        if call.rank == Rank.OPERATOR:
            e = self.__dispatch__(call, self.operators)
        elif call.rank == Rank.SUPERVISOR:
            e = self.__dispatch__(call, self.supervisors)
        elif call.rank == Rank.DIRECTOR:
            e = self.__dispatch__(call, self.directors)
        if e is None:
            self.queued_calls[call.rank].append(call) # queue it, not secessful

    def __dispatch__(self, call, employees):
        for e in employees:  # search the line for taking calls, get person
            if e.call is None:
                e.take_call(call)
                return e
        return None

    def notify_call_completed(self, call):
        if self.queued_calls[call.rank]:
            wait_call = self.queued_calls[call.rank].popleft()
            self.dispatch_queued_call_to_newly_free(wait_call, call.employee)

    def notify_call_escalated(self, call):
        pass

    def dispatch_queued_call_to_newly_free(self, call, employee):
        employee.take_call(call)





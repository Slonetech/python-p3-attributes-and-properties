#!/usr/bin/env python3



class Person:
    APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
 ]
   
    def get_name(self):
        return self._name

    def set_name(self, name):
        if (type(name) == str) and (1 <= len(name) <= 25):
            print(f"Setting name to {name}")
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in Person.APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    name = property(get_name, set_name)
    job = property(get_job, set_job)
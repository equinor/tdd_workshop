# Search more about:
* Value objects
* aliasing
* functional code
- pytest (https://docs.pytest.org/) x unittest
- Fixtures e.g. @pytest.fixture(scope="module")
- Parametrizing
- hypothesis (https://github.com/equinor/camille/blob/c60e767eb4802a6a9c0b9134bdd5940620ed410b/tests/process/test_lidar.py#L107), https://hypothesis.readthedocs.io/en/latest/
- pytest-timeout (https://pypi.org/project/pytest-timeout/)
- Monkeypatching (https://docs.pytest.org/en/stable/monkeypatch.html)
- mock side effects
- test coverage (codecov), in PR
- mutation testing (time consuming) mutmut (petroelastic example 6000 mutations, time consuming, at night Andreas team)
- @property
- integration test (NASA example)
- triangle testing: units/functional/integration (time, coverage)
https://www.softwaretestinghelp.com/the-difference-between-unit-integration-and-functional-testing/

# Problems solved
- Testing in VSC was different from pycharm:
https://stackoverflow.com/questions/65577254/python-module-import-statement-runs-in-pycharm-but-not-in-vscode
- "python -m venv tdd_venv" leads to "Error: [WinError 1260] This program is blocked by group policy. For more information, contact your system administrator"

# For data scientists
https://medium.com/miq-tech-and-analytics/test-driven-development-in-data-science-190f1247ebbc

https://www.linkedin.com/pulse/software-engineering-data-scientist-test-driven-gopinadhan-jagan-/
python modules -> jupyter

# Example of dependency injection & mocking

Often, complicated dependencies make testing difficult or time consuming.
To remedy this, there are generally two strategies: dependency injection
and mocking.

## Dependency Injection

Dependency injection is mostly just a fancy name for passing parameters. What
we are doing is substitution one object/value/service used in production
with a one or more used only for testing.

Say you have the following function:

```python
import datetime

def after_one_o_clock() -> bool:
    return datetime.now().hour > 13
```

while possible to test:

```python

def test_after_one_o_clock():
    if after_one_o_clock():
        assert datetime.now().hour > 13
    else:
        assert datetime.now().hour <= 13
```

the test just repeats the implementation and a failure may depend on the time
of day the test is run making it hard to reproduce. Also, technically, not all
computers have a persisted clocks and can tell you the current time. So instead
we can pass the time as a parameter:

```python
import datetime

def after_one_o_clock(time: datetime) -> bool:
    return time.hour > 13
```

which is very easy to test:


```python

def test_after_one_o_clock():
    assert after_one_o_clock(datetime.fromisoformat("2020-09-93T20:56:35"))
    assert not after_one_o_clock(datetime.fromisoformat("1918-11-11T11:00:00"))
```

## Mocking

Mocking is the practice of creating an object, only ment for testing that
we dependency inject. So lets say we have a procedure that charges
a credit card:

```python
import datetime

COST_OF_SPAM = ...

def buy_spam(customer) -> bool:
    customer.credit_card.charge(COST_OF_SPAM)
    ...
```

In order to test this, we don't want the test
to actually charge a credit card every time we run
the test so we create a mock customer with a mock
credit card.

```python

class MockCreditCard:
    def __init__(self):
        charged = 0.0

    def charge(self, cost):
        charged += cost

class MockCustomer:
    def __init__(self):
        self.credit_card = MockCreditCard

def test_buying_spam_charges_the_customer_the_cost_of_spam():
    customer = MockCustomer()
    buy_spam(customer)
    assert customer.credit_card.charged == COST_OF_SPAM
```

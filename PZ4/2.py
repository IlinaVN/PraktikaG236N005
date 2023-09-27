import pulp

x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
x3 = pulp.LpVariable("x3", lowBound=0)
x4 = pulp.LpVariable("x4", lowBound=0)
problem = pulp.LpProblem('0', pulp.LpMaximize)
problem += x1 + x2 + x3 - x4, "Максимум"
problem += x1 + x2 + 2 * x3 + x4 == 12, "1"
problem += x1 + 2 * x2 + x3 <= 20, "2"
problem += x1 + x2 + x3 <= 20, "3"
problem.solve()
print("Максимум:")
print(pulp.value(problem.objective))

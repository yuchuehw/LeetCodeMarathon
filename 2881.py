import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
  employees.insert(2, "bonus", employees.get("salary")*2)
  return employees
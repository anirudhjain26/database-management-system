from menu import getTotalSales
from employees import getSalCost
from inventory import getInvCost


def getProfit():
    return getTotalSales - getSalCost - getInvCost

def getSales():
    return getTotalSales

def getCost():
    return getInvCost + getSalCost
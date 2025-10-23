# Exploring the module oldcoins
from Old_coins import OldCoinsStash

stash_ragnar = OldCoinsStash("Ragnar Lothbroke")
stash_ragnar.deposit(100, 500)
print(stash_ragnar.check_balance())

stash_ragnar.withdraw(20, 200)
print(stash_ragnar.check_balance())

stash_bjorn = OldCoinsStash("Bjorn")
print(stash_bjorn)







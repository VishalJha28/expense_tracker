# expense_tracker
### This is a python script developed for a simplistic expense tracker. 
### Use Pydroid to run it on android. 
### The entry point will be main.py and you would be able to track expenses, view charts, see on an accrual basis how much you have spent etc.

Usage:
In the main screen you will have a form - 
- Amount:
- Description:
- Category: (To modify categories, go to ui.py)
- Useful life (in days): If you make a purchase like a car, you wouldn't be using it up in 1 day and hence don't want that days expense to be ridiculously high.
  So you have the option to split it over multiple days (the useful life of the purchase). 
  There are category wise default useful life days configured in ui.py or you can manually enter when saving a new expense
- Mark as asset is a feature to separate your investments from expenditure. So any purchase that you value as an asset can be added here and will show up in the total assets on the accrual page

def si(no_of_years, principal_amt, rate):
    interest = float((no_of_years * principal_amt * rate) / 100)
    return interest


p = int(input('Enter principle amount  : '))
n = int(input('Enter Time period : '))
r = int(input('Enter Rate of interest : '))

print('Simple Interest : ', si(n, p, r))

number = -7605
sorted_number = ''.join(sorted(str(abs(number)), reverse=True))
print(sorted_number)
arranged_number = int(sorted_number) * -1 if number < 0 else int(sorted_number)
print(arranged_number)

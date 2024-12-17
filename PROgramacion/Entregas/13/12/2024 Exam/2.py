from colorama import Fore, Style
temperatures= [[22,24,19,21,25,23,20], #week 1
               [20,22,21,23,24,22,21], #week 2
               [23,21,20,22,24,25,23]] #week 3
temperature1= [22,24,19,21,25,23,20]
temperature2= [20,22,21,23,24,22,21]
temperature3=[23,21,20,22,24,25,23]
average1=sum(temperature1)/7 #average of each week
average2=sum(temperature2)/7
average3=sum(temperature3)/7
sort1=sorted(temperature1) #sorts the numbers of the list of each week to say then the last element of the list (the hottest)
sort2=sorted(temperature2)
sort3=sorted(temperature3)
print(Fore.GREEN + f'Average (week 1, 2 and 3 respectively): {average1:.2f}, {average2:.2f}, {average3:.2f}.' + Style.RESET_ALL)
print(Fore.RED + f'Hottest day of each week (week 1, 2 and 3 respectively): {sort1[6]}, {sort2[6]}, {sort3[6]}.' + Style.RESET_ALL)

# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
numbers = {'0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
           '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '10': 'Ten',
           '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen',
           '15': 'Fifteen', '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen',
           '20': 'Twenty', '30': 'Thirty', '40': 'Forty', '50': 'Fifty', '60': 'Sixty', '70': 'Seventy', '80': 'Eighty',
           '90': 'Ninety',
           '100': 'Hundred', '1000': 'Thousand', '1000000': 'Million', '1000000000': 'Billion'}
names = ['Hundred', 'Thousand', 'Million', 'Billion', 'Trillion']


def f(x):
    return {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '0': 0,
    }[x]


for a0 in xrange(t):
    n = raw_input().strip()
    # print n
    x = len(n)
    i = x - 1
    final = ''
    j = 0
    if n == '0':
        print 'Zero'
    else:
        while i >= 0:
            ans = ''
            if (i - 2) >= 0 and n[i - 2] != '0':
                # print 'inside 1'
                ans = ans + numbers[n[i - 2]] + ' ' + names[0] + ' '
            if (i - 1) >= 0 and n[i - 1] == '1':
                # print 'i/nside 2'
                ans = ans + numbers[n[i - 1:i + 1]]
                ans = ans + ' '
            elif (i - 1) >= 0 and n[i - 1] != '0':
                # print 'inisde 3'
                ans = ans + numbers[n[i - 1] + '0'] + ' ' + numbers[n[i]] + ' '
            elif n[i] != '0':
                # print 'inside 4'
                ans = ans + numbers[n[i]]
                ans = ans + ' '
            # print i
            # print '----------'
            if (i - 2) >= 0 and (i - 1) >= 0:
                # print i
                if n[i - 1] != '0' or n[i - 2] != '0' or n[i] != '0':
                    # print 'inside this'
                    if j != 0:
                        ans = ans + names[j]
            elif (i - 1) >= 0:
                if n[i - 1] != '0' or n[i] != '0':
                    if j != 0:
                        ans = ans + names[j]
            else:
                if j != 0:
                    ans = ans + names[j]
            if ans != '':
                final = ' ' + ans + final
            j = j + 1
            i = i - 3
        if final[0] == ' ':
            final = final[1:]
        y = len(final)
        if y > 0 and final[y - 1] == ' ':
            # print 'inside'
            final = final[:y]
            print final
        else:
            print final


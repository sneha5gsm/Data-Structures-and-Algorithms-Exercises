/ *
// Sample
code
to
perform
I / O:

process.stdin.resume();
process.stdin.setEncoding("utf-8");
var
stdin_input = "";

process.stdin.on("data", function(input)
{
    stdin_input += input; // Reading
input
from STDIN
});

process.stdin.on("end", function()
{
    main(stdin_input);
});

function
main(input)
{
    process.stdout.write("Hi, " + input + ".\n"); // Writing
output
to
STDOUT
}

// Warning: Printing
unwanted or ill - formatted
data
to
output
will
cause
the
test
cases
to
fail
* /

var
readline = require('readline');
// Write
your
code
here
process.stdin.resume();
process.stdin.setEncoding("utf-8");
var
n = 0
var
z = 0
var
arr = []

var
rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

rl.on('line', function(line)
{
if (z == 0)
{
    n = parseInt(line);
z = 1
}
else {
     // console.log('inside else')
arr = line.split(' ').map(function(item)
{
return parseInt(item, 10);
});
// console.log(arr)
}
// console.log(line);
// console.log(n)
   // console.log(arr)
})
// process.stdin.on("data", function(input)
{
// var
input_stdin_array = input.split("\n");
// n = parseInt(input_stdin_array[0].strip())
       // arr = input_stdin_array[1].strip().split(' ').map(function(item)
{
//
return parseInt(item, 10);
//});
// // Reading
input
from STDIN
//});

process.stdin.on("end", function()
{
    main();
});

function
main()
{
    var
total = 1;
flag = 0
       // console.log(arr)
for (var i=1;i < (n-1); i++)
{
// console.log('inside')
// console.log(arr[i])
if (arr[i] == -1){
total = total * parseInt((arr[i-1] + arr[i+1]) / 2)
// console.log(total)
total =total % 1000000007
// console.log(total)
}
}
total = total % 1000000007
console.log(total)
}


var alpha = {'a':0, 'b':1, 'c':1, 'd':1,'e':0, 'f':1, 'g':1, 'h':1, 'i':0, 'j':1, 'k':1, 'l':1, 'm':1,
'n':1, 'o':0,'p':1,'q':1,'r':1,'s':1,'t':1,'u':0,'v':1,'w':1,'x':1,'y':1,'z':1
}





var
readline = require('readline');
// Write
your
code
here
process.stdin.resume();
process.stdin.setEncoding("utf-8");
var
n = 0
var
f = 0
var
arr = []

var
rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

rl.on('line', function(line)
{
if (f == 0)
{
    n = parseInt(line);
f = 1
}
else {
     // console.log('inside else')
arr = line.split(' ').map(function(item)
{
return parseInt(item, 10);

});
// console.log(arr)
var
n = arr[0]
var
a = arr[1]
var
b = arr[2]
var
c = arr[3]
if (a == b & & b == c)
{
    console.log('0')
}
else {
    var
lcms = [lcm(a, b), lcm(b, c), lcm(a, c)].sort((a, b) = > a - b)
// console.log(lcms)
var
total = parseInt(n / a) + parseInt(n / b) + parseInt(n / c)
        // console.log(total)
if (lcms[0] == lcms[1] & & lcms[1] == lcms[2])
{
total = total - 3 * parseInt(n / lcms[0])
console.log(total)
}
else {
var
x = lcms[0]
total = total - 2 * parseInt(n / x)
var
y = lcms[1]
if (x != y){
if (y % x == 0)
{
// console.log('insideeee 1')
total = total -parseInt(n / y)
}
else {
// console.log('inseiidee 2')
total = total -2 * parseInt(n / y)
}
}
var
z = lcms[2]
if (z != y & & z != x)
    {
    if (z % y == 0 & & z % x == 0)
    {
        total = total + parseInt(n / z)
    }
    else if (z % y == 0 | | z % x == 0)
    {
    // console.log('1111')
    total = total -parseInt(n / z)
    }
    else {
    // console.log('2222')
    total = total -2 * parseInt(n / z)
    }
    }

if (total < 0)
    {
    // console.log('inisdeee')
    // console.log(total)
    total = 0
    }
    console.log(total)}
    }}
    })
    function
    gcd(a, b)
    {
    return !b ? a: gcd(b, a % b);
    }

    function
    lcm(a, b)
    {
    return (a * b) / gcd(a, b);
    }


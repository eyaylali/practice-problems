# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the
# number and for the multiples of five print “Buzz”. For
# numbers which are multiples of both three and five
# print “FizzBuzz”.

(1..100).each do |x|
  if x % 5 == 0 && x % 3 ==0
    print "FizzBuzz"  
  elsif x % 3 == 0
    print "Fizz"
  elsif x % 5 == 0
    print "Buzz"
  else 
    print x
  end
end
  
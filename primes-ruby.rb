#Write a method, is_prime?, that takes a number num and returns true if it is prime and false otherwise.


 def is_prime?(num)
  (2...num).each do |x|
    if num % x == 0
      return false
    end
  end
    true
end

puts is_prime?(3)
puts is_prime?(4)
puts is_prime?(15)
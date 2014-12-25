#Write a method, sum which takes an array of numbers and returns the sum of the numbers. 
  
  
 def sum(array)
   sum = 0
   
   (0...array.length).each do |i|
     sum += array[i]
   end
   sum
 end
 
 puts sum([1,2,3])
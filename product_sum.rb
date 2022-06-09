def product_sum(array)
  product_summer(array, 1)
end

def product_summer(array, depth)
  sum = 0

  array.each do |item|
    sum += if item.instance_of?(Integer)
      item
    else
      product_summer(item, depth + 1)
    end
  end

  sum * depth
end

puts product_sum([1, 2, 3]) #=> 6
puts product_sum([1, 2, [3]]) #=> 9

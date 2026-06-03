from monte_carlo_funcs import create_strings, select_ends, tie_ends

# Run the Monte Carlo
list_of_circles = []
num_strings = 50
num_simulations = 10000

if __name__ == "__main__":
  for _ in range(0, num_simulations):
      
      # create the simulated starting box of strings
      strings = create_strings(num_strings)
  
      # start circle counter for this simulation
      circle_counter = 0
  
      # draw from the box until there are no more strings left
      while len(strings) > 0:
          end_1, end_2, strings = select_ends(strings)
          strings, circle_bool = tie_ends(strings, end_1, end_2)
          circle_counter += circle_bool
          
      # add the number of circles that counts number of circles for each round
      list_of_circles.append(circle_counter)
  
  print(np.mean(list_of_circles))

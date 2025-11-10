def approximate_pi (n_terms):
  total=0
  for n in range (n_terms):
    total+=((-1)**2/(2*n+1))
  return 4*total
    

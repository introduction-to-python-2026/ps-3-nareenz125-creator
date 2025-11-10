def approximate_pi (n_terms):
    pi_estimate = 0
    for n in range(n_terms):
        pi_estimate += ((-1)**) / (2*n + 1)
    pi_estimate *= 4
    return pi_estimate

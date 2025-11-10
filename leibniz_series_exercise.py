def approximate_pi(n_terms):
    pi_estimate = 0
    for n in range(n_terms):
        pi_estimate += ((-1)**n) / (2*n + 1)
    pi_estimate *= 4
    return pi_estimate


for terms in [1, 10, 100, 1000, 10000]:
    print(f"{terms} terms: {approximate_pi(terms)}")

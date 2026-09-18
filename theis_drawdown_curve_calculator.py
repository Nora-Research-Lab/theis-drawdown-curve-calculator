import numpy as np
import math

def exp1_approximation(u):
    """
    Approximate the exponential integral E1(u) using series expansion
    W(u) = -γ - ln(u) + u - u²/(2×2!) + u³/(3×3!) - u⁴/(4×4!) + ...
    where γ ≈ 0.5772156649015329 is the Euler-Mascheroni constant
    """
    if u <= 0:
        return float('inf')
    
    gamma = 0.5772156649015329  # Euler-Mascheroni constant
    result = -gamma - math.log(u)
    
    term = 1.0
    n = 1
    while abs(term) > 1e-9:
        term = ((-1)**n) * (u**n) / (n * math.factorial(n))
        result += term
        n += 1
    
    return result

def calculate_theis_drawdown(T, S, Q, r, t_max, N):
    """
    Calculate Theis drawdown curve based on provided parameters.
    
    Parameters:
    - T: Transmissivity (m²/day)
    - S: Storativity (dimensionless)
    - Q: Pumping rate (m³/day)
    - r: Radial distance from pumping well (m)
    - t_max: Maximum pumping time (days)
    - N: Number of points to calculate
    
    Returns:
    - A pandas DataFrame with columns: time, u, W_u, drawdown
    """
    import pandas as pd
    
    # Generate logarithmically spaced time values
    min_time = max(1e-4, t_max / 1000)
    times = np.logspace(np.log10(min_time), np.log10(t_max), num=N)
    
    # Initialize lists to store results
    u_values = []
    W_u_values = []
    drawdown_values = []
    
    # Try to use scipy for more accurate calculation
    try:
        from scipy.special import exp1
        use_scipy = True
    except ImportError:
        use_scipy = False
    
    for t in times:
        # Calculate the auxiliary variable u
        u = (r**2 * S) / (4 * T * t)
        u_values.append(u)
        
        # Evaluate the Theis well function W(u)
        if use_scipy:
            W_u = exp1(u)
        else:
            W_u = exp1_approximation(u)
        W_u_values.append(W_u)
        
        # Calculate drawdown
        drawdown = (Q / (4 * np.pi * T)) * W_u
        drawdown_values.append(drawdown)
    
    # Create a DataFrame with results
    results_df = pd.DataFrame({
        'time': times,
        'u': u_values,
        'W_u': W_u_values,
        'drawdown': drawdown_values
    })
    
    return results_df

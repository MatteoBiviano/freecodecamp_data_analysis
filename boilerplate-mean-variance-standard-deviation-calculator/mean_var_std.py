import numpy as np

def calculate(list):
  if len(list) == 9:
    matrix = np.reshape(list, (3,3))
    calculations = {"mean":[np.mean(matrix,0).tolist(),np.mean(matrix,1).tolist(),np.mean(matrix).tolist()],
    				  "variance":[np.var(matrix,0, dtype=np.float64).tolist(),np.var(matrix,1).tolist(),np.var(matrix).tolist()],
    				  "standard deviation":[np.std(matrix,0).tolist(),np.std(matrix,1).tolist(),np.std(matrix).tolist()],
    				  "max":[np.max(matrix,0).tolist(),np.max(matrix,1).tolist(),np.max(matrix).tolist()],
    				  "min":[np.min(matrix,0).tolist(),np.min(matrix,1).tolist(),np.min(matrix).tolist()],
    				  "sum":[np.sum(matrix,0).tolist(),np.sum(matrix,1).tolist(),np.sum(matrix).tolist()]}
    return calculations
  else:
    raise ValueError ('List must contain nine numbers.')


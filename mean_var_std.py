import numpy as np

def calculate(list):
  
      try:
        np_list=np.array(list).reshape(3,3)
      except:
        raise ValueError("List must contain nine numbers.")    
      
      calculations={'mean':[np_list.mean(axis=0).tolist(),np_list.mean(axis=1).tolist(),np_list.mean().tolist()],'variance':[np_list.var(axis=0).tolist(),np_list.var(axis=1).tolist(),np_list.var().tolist()],
                      'standard deviation':[np_list.std(axis=0).tolist(),np_list.std(axis=1).tolist(),np_list.std().tolist()],
                      'max':[np_list.max(axis=0).tolist(),np_list.max(axis=1).tolist(),np_list.max().tolist()],
                      'min':[np_list.min(axis=0).tolist(),np_list.min(axis=1).tolist(),np_list.min().tolist()],
                      'sum':[np_list.sum(axis=0).tolist(),np_list.sum(axis=1).tolist(),np_list.sum().tolist()]}

      return calculations
    
   
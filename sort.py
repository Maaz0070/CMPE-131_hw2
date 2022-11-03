def sort_dictionary(dict):
      sorted_keys = sorted(dict.keys(), key = lambda x: dict[x][1])
      result = []
      
      for k in sorted_keys:
            tuple = (k, dict[k][0])
            result.append(tuple)
            
      return result 
  
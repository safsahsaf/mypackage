def top_n (items,n):
    """Return the top n items in an array , in desc order.

    Args: 
    items (array): list or array like object
    n(int): num of items to Return

    Return:
     array : top n items, in desc order

     Egs:
      >>> top_n([8,3,2,7,4],3)
      [8,7,3]
      """
      for in in range(n):
          for j in range(len(items)-1-i):

              if items[j]> items[j+1]:
                  items [j], items[j+1]= items[j+1], items[j]

                  top_n= items[-n:]

                  Return top_n[[::-1]

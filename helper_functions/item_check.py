def item_check(Items):
  if len(Items) > 0:
    selected_item = Items.pop()
    return [selected_item]
  else:
    return []
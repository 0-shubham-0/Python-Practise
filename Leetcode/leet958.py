def something(root):
    have_null = False
    Q = [root]
    
    while Q:
        cur_node = Q.pop(0)
        if not cur_node: 
            have_null = True
            continue
        if have_null: return False
        Q.append(cur_node.left)
        Q.append(cur_node.right)
        
    return True

a=-1
if a:
    print("a is true")
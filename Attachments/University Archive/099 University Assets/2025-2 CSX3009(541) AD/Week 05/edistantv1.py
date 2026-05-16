# Puran Paodensakul
# 6611140
# 541

def edistantv1(a, b):

    if not a:
        return len(b)
    if not b:
        return len(a)

    if a[0] == b[0]:
        return edistantv1(a[1:], b[1:])
    
    insert_cost = 1 + edistantv1(a, b[1:])
    delete_cost = 1 + edistantv1(a[1:], b)
    substitute_cost = 1 + edistantv1(a[1:], b[1:])
    
    return min(insert_cost, delete_cost, substitute_cost)

if __name__ == '__main__':
    string_a = input()
    string_b = input()
    print(edistantv1(string_a, string_b))

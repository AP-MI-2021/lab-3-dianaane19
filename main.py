def alternate_signs(list):
    '''
    Verifica daca semnele elem listei sunt alternante
    :param list: lista de nr intregi
    :return: True daca semnele elem sunt alternante si False, altfel
    '''
    for el in range(1, len(list)):
        if list[el] * list[el-1] > 0:
            return False
    return True

def get_longest_alternating_signs(list):
    '''
    Prezinta elem listei unde semnele se alterneaza
    :param list: lista de nr intregi
    :return: lista cu elem unde semnele se alterneaza
    '''
    smax = []
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if alternate_signs(list[i:j+1]) and len(list[i:j+1]) > len(smax):
                smax = list[i:j+1]
    return smax

def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([1, -2, 3, -4, 5]) == [1, -2, 3, -4, 5]
    assert get_longest_alternating_signs([2, 3, -6]) == [3, -6]

def is_prime_list(list):
    '''
    Verifica el prime dintr-o lista
    :param list: lista de nr intregi
    :return: True daca el este prim si False, altfel
    '''
    for el in range(1, len(list)):
        if (list[el]==0 or list[el]==1):
            return False
        for d in range(2, list[el]//2):
            if (list[el]%d==0):
                return False
    return True

def get_longest_all_primes(list):
    '''
    Prezinta elem listei unde elem sunt nr prime
    :param list: lista de nr intregi
    :return: lista cu elem care sunt nr prime
    '''
    sprim = []
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if is_prime_list(list[i:j+1]) and len(list[i:j+1]) > len(sprim):
                sprim = list[i:j+1]
    return sprim

def test_get_longest_all_primes():
    assert get_longest_all_primes([1, 3, 6]) == [1, 3]

def is_prime(n):
    '''
    Verifica n nr prim
    :param n: nr intreg
    :return: True daca n este prim si False, altfel
    '''
  if (n==0 or n==1):
    return False
  for d in range(2, n//2):
    if (n%d==0):
      return False
    return True

def cif_is_prime(list):
    '''
    Verifica daca elem listei sunt form din nr cu cifre prime
    :param list: lista de nr intregi
    :return: True daca elem sunt nr cu cifre prime si False, altfel
    '''
    for el in list:
        while el!=0:
            cif = el % 10
            el = el // 10
            if is_prime(cif) == False:
                return False
    return True

def get_longest_prime_digits(list):
    '''
    Prezinta elem listei unde elem sunt nr form din cifre prime
    :param list: lista de nr intregi
    :return: lista cu elem care sunt nr form din cifre prime
    '''
    scif = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            if cif_is_prime(list[i:j+1]) and len(list[i:j+1]) > len(scif):
                scif = list[i:j+1]
    return scif

def test_get_longest_prime_digits():
    assert get_longest_prime_digits([13, 22, 40]) == [22]
    assert get_longest_prime_digits([10, 11]) == []

def show_menu():
    print('''
    1. Citire listă
    2. Numerele au semne alternante
    3. Toate numerele sunt prime
    4. Toate numerele sunt formate din cifre prime
    0. Ieșire
    ''')

def read_list():
    list = []
    n = int(input("Introduceți numărul de elem din listă:"))
    for i in range(n):
        x = int(input("a[{}]=".format(i + 1)))
        list.append(x)
    return list

def main():
    test_get_longest_alternating_signs()
    test_get_longest_all_primes()
    test_get_longest_prime_digits()
    list = []
    while True:
        show_menu()
        cmd = input("Comandă:")
        if cmd == '1':
            list = read_list()
        elif cmd == '2':
            rez1 = get_longest_alternating_signs(list)
            print(rez1)
        elif cmd == '3':
            rez2 = get_longest_all_primes(list)
            print(rez2)
        elif cmd == '4':
            rez3 = get_longest_prime_digits(list)
            print(rez3)
        elif cmd == '0':
            break
        else:
             print("Comandă invalidă")

main()
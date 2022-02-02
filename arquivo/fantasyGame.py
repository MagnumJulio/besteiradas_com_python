#Inventário de um jogo fantasia 

def displayInventory(inventory_ref):
    count_items = 0
    print('Inventory:')
    for k, v in (inventory_ref.items()):
        count_items += v
        print(f'{v} {k}')

    print(f'Total number of items: {count_items}')

def addToInventory(inventory_ref, addedItems_ref):
    for i in addedItems_ref:
            inventory_ref.setdefault(i, 0) #só cria a chave com o valor dado se esta não existir
            inventory_ref[i] += 1            
    # print(f'{inventory_ref}')
    


inventory = {'rope':  1,  'torch':  6,  'gold coin':  42,
    'dagger':  1,  'arrow':  12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', "ruby"]


addToInventory(inventory, dragonLoot)
displayInventory(inventory)
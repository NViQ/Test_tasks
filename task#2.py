def update_collections(N, M, Q, A_cards, B_cards, changes):
    results = []

    for change in changes:
        type_change, player, card = change
        card = int(card)

        if player == 'A':
            if type_change == 1:
                A_cards.append(card)
            elif type_change == -1 and card in A_cards:
                A_cards.remove(card)
        elif player == 'B':
            if type_change == 1:
                B_cards.append(card)
            elif type_change == -1 and card in B_cards:
                B_cards.remove(card)

        remaining_cards = len([c for c in A_cards if c not in B_cards]) + len([c for c in B_cards if c not in A_cards])
        results.append(remaining_cards)

    return results


# N, M, Q = 2, 5, 10
# A_cards = [1, 2]
# B_cards = [1, 2, 3, 4, 5]
# changes = [
#     (1, 'A', 3), (1, 'A', 4), (1, 'A', 5),
#     (1, 'A', 6), (1, 'A', 7), (-1, 'A', 1),
#     (1, 'B', 7), (-1, 'A', 6), (-1, 'B', 1),
#     (1, 'A', 7)
# ]
#
# print(update_collections(N, M, Q, A_cards, B_cards, changes))

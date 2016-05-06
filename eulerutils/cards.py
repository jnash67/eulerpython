
# hearts, clubs, spades, diamonds
card_suits = ['H', 'C', 'S', 'D']
card_values = dict()
card_values['2']=2
card_values['3']=3
card_values['4']=4
card_values['5']=5
card_values['6']=6
card_values['7']=7
card_values['8']=8
card_values['9']=9
card_values['T']=10
card_values['J']=11
card_values['Q']=12
card_values['K']=13
card_values['A']=14

number_cards = ['2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'T']
picture_cards = ['J' , 'Q' , 'K' , 'A']

hand_types = dict()
hand_types['Royal Flush']=10
hand_types['Straight Flush']=9
hand_types['Four of a Kind']=8
hand_types['Full House']=7
hand_types['Flush']=6
hand_types['Straight']=5
hand_types['Three of a Kind']=4
hand_types['Two Pairs']=3
hand_types['One Pair']=2
hand_types['High Card']=1


def is_card_greater_or_equal(card, cardToCompareTo):
    if is_card_greater(card, cardToCompareTo):
        return True
    elif is_card_equal(card, cardToCompareTo):
        return True
    else:
        return False


def is_card_equal(card, cardToCompareTo):
    if card is None and cardToCompareTo is None:
        print("Attempt to compare two None cards which returns that they are equal")
        return True
    card1Val = card_values[card[0]]
    card2Val = card_values[cardToCompareTo[0]]
    return card1Val == card2Val


def is_card_greater(card, cardToCompareTo):
    # we can get a None cardTocompareTo from highest_value_card
    if card is not None and cardToCompareTo is None:
        return True
    if card is None and not cardToCompareTo is None:
        print("Attempt to compare first card None to actual card. Actual card is bigger")
        return False
    if is_card_equal(card, cardToCompareTo):
        return False

    card1Val = card_values[card[0]]
    card2Val = card_values[cardToCompareTo[0]]
    return card1Val > card2Val


def higher_card(card1,card2):
    if is_card_greater_or_equal(card1,card2):
        return card1
    else:
        return card2


def lower_card(card1, card2):
    if is_card_greater_or_equal(card1,card2):
        return card2
    else:
        return card1


def are_cards_consecutive(card, cardToCompareTo):
    card1Val = card_values[card[0]]
    card2Val = card_values[cardToCompareTo[0]]
    if abs(card1Val-card2Val)==1:
        return True
    else:
        return False


# takes a list or set of cards e.g. 5H 5C 6S 7S KD
def highest_value_card(possiblyUnsortedHand):
    highestSoFar = None
    for card in possiblyUnsortedHand:
        if is_card_greater(card, highestSoFar):
            highestSoFar = card
    return highestSoFar


def sort_hand(hand):
    l = len(hand)
    for j in range(0, l-1):
        for i in range(0, l-1):
            if is_card_greater(hand[i], hand[i + 1]):
                hand[i], hand[i + 1] = hand[i + 1], hand[i]


# functions that check if a hand is of a particular type, return None if it is not
# and a tuple of the highest card of the type (e.g. of the two pairs) and the highest
# tie break card

def does_first_hand_win(hand1, hand2):
    sort_hand(hand1)
    sort_hand(hand2)
    resultTuple1 = hand_value(hand1)
    resultTuple2 = hand_value(hand2)
    hv1 = resultTuple1[0]
    hv2 = resultTuple2[0]
    if hv1 > hv2:
        return True
    elif hv1 == hv2:
        if hv1 == 10:
            raise ValueError("According to euler prob 54 we don't know how to resolve a royal flush tie. All suits have same value.")
        elif hv1 == 9:
            startOfStraightFlush1 = resultTuple1[1][0]
            startOfStraightFlush2 = resultTuple2[1][0]
            if is_card_equal(startOfStraightFlush1, startOfStraightFlush2):
                raise ValueError("According to euler prob 54 we don't know how to resolve a straight tie. All suits have same value.")
            elif is_card_greater(startOfStraightFlush1, startOfStraightFlush2):
                return True
            else:
                return False
        elif hv1 == 8:
            fourOfAKindCard1 = resultTuple1[1][0]
            fourOfAKindCard2 = resultTuple2[1][0]
            if is_card_equal(fourOfAKindCard1, fourOfAKindCard2):
                raise ValueError("This should not be possible.  Can't have a tie with two four of a kind.")
            elif is_card_greater(fourOfAKindCard1, fourOfAKindCard2):
                return True
            else:
                return False
        elif hv1 == 7:
            fullHouseCard1 = resultTuple1[1][0]
            fullHouseCard2 = resultTuple2[1][0]
            if is_card_equal(fullHouseCard1, fullHouseCard2):
                raise ValueError("This should not be possible.  Can't have a tie with two full house.")
            elif is_card_greater(fullHouseCard1, fullHouseCard2):
                return True
            else:
                return False
        elif hv1 == 6:
            # it all comes down to which cards are higher
            # we send copies since this can alter the hand
            return does_first_hand_win_tie_break(list(hand1), list(hand2))
        elif hv1 ==5:
            startOfStraightCard1 = resultTuple1[1][0]
            startOfStraightCard2 = resultTuple2[1][0]
            if is_card_equal(startOfStraightCard1, startOfStraightCard2):
                raise ValueError("According to euler prob 54 we don't know how to resolve a straight tie. All suits have same value.")
            elif is_card_greater(startOfStraightCard1, startOfStraightCard2):
                return True
            else:
                return False
        elif hv1 ==4:
            threeOfAKindCard1 = resultTuple1[1][0]
            threeOfAKindCard2 = resultTuple2[1][0]
            if is_card_equal(threeOfAKindCard1, threeOfAKindCard2):
                raise ValueError("This should not be possible.  Can't have a tie with two three of a kind.")
            elif is_card_greater(threeOfAKindCard1, threeOfAKindCard2):
                return True
            else:
                return False
        elif hv1 ==3:
            highestOfTwoPairsCard1 = resultTuple1[1][0]
            highestOfTwoPairsCard2 = resultTuple2[1][0]
            if is_card_equal(highestOfTwoPairsCard1, highestOfTwoPairsCard2):
                # compare the other pair
                lowestOfTwoPairsCard1 = resultTuple1[1][1]
                lowestOfTwoPairsCard2 = resultTuple2[1][1]
                if is_card_equal(lowestOfTwoPairsCard1, lowestOfTwoPairsCard2):
                    # compare the last card
                    lastCard1 = resultTuple1[1][2]
                    lastCard2 = resultTuple2[1][2]
                    if is_card_equal(lastCard1, lastCard2):
                        raise ValueError("According to euler prob 54 we don't know how to resolve a two pair tie. All suits have same value.")
                    elif is_card_greater(lastCard1, lastCard2):
                        return True
                    else:
                        return False
                elif is_card_greater(lowestOfTwoPairsCard1, lowestOfTwoPairsCard2):
                    return True
                else:
                    return False
            elif is_card_greater(highestOfTwoPairsCard1, highestOfTwoPairsCard2):
                return True
            else:
                return False
        elif hv1 ==2:
            highestOfOnePairCard1 = resultTuple1[1][0]
            highestOfOnePairCard2 = resultTuple2[1][0]
            if is_card_equal(highestOfOnePairCard1, highestOfOnePairCard2):
                remainingHand1 = []
                remainingHand1.append(resultTuple1[1][1])
                remainingHand1.append(resultTuple1[1][2])
                remainingHand1.append(resultTuple1[1][3])
                remainingHand2 = []
                remainingHand2.append(resultTuple2[1][1])
                remainingHand2.append(resultTuple2[1][2])
                remainingHand2.append(resultTuple2[1][3])
                return does_first_hand_win_tie_break(remainingHand1, remainingHand2)
            elif is_card_greater(highestOfOnePairCard1, highestOfOnePairCard2):
                return True
            else:
                return False
        elif hv1 == 1:
            # it all comes down to which cards are higher
            # we send copies since this can alter the hand
            return does_first_hand_win_tie_break(list(hand1), list(hand2))
    else:
        return False


def hand_value(sortedhand):
    resultTuple = is_royal_flush(list(sortedhand))
    if not(resultTuple is None):
        return hand_types['Royal Flush'], resultTuple
    else:
        resultTuple = is_straight_flush(list(sortedhand))
        if not(resultTuple is None):
            return hand_types['Straight Flush'], resultTuple
        else:
            resultTuple = is_four_of_a_kind(list(sortedhand))
            if not(resultTuple is None):
                return hand_types['Four of a Kind'], resultTuple
            else:
                resultTuple = is_full_house(list(sortedhand))
                if not(resultTuple is None):
                    return hand_types['Full House'], resultTuple
                else:
                    resultTuple = is_flush(list(sortedhand))
                    if not(resultTuple is None):
                        return hand_types['Flush'], resultTuple
                    else:
                        resultTuple = is_straight(list(sortedhand))
                        if not(resultTuple is None):
                            return hand_types['Straight'], resultTuple
                        else:
                            resultTuple = is_three_of_a_kind(list(sortedhand))
                            if not(resultTuple is None):
                                return hand_types['Three of a Kind'], resultTuple
                            else:
                                resultTuple = is_two_pairs(list(sortedhand))
                                if not(resultTuple is None):
                                   return hand_types['Two Pairs'], resultTuple
                                else:
                                    resultTuple = is_one_pair(list(sortedhand))
                                    if not(resultTuple is None):
                                       return hand_types['One Pair'], resultTuple
                                    else:
                                        return hand_types['High Card'], list(sortedhand)


def does_first_hand_win_tie_break(sortedhand1, sortedhand2):
    while sortedhand1!=[]:
        hv1 = sortedhand1.pop()
        hv2 = sortedhand2.pop()
        if is_card_greater(hv1, hv2):
            return True
        elif not is_card_equal(hv1, hv2):
            return False
    raise ValueError("According to euler prob 54 we don't know how to resolve a full tie. All suits have same value.")


# return a 4-tuple needed to compare
def is_one_pair(sortedhand):
    card1 = sortedhand[0]
    card2 = sortedhand[1]
    card3 = sortedhand[2]
    card4 = sortedhand[3]
    card5 = sortedhand[4]
    if (card1[0] == card2[0]) and (card1[0] != card3[0] != card4[0] != card5[0]):
        sortedhand.remove(card1)
        sortedhand.remove(card2)
        return card1, card3, card4, card5
    elif (card2[0] == card3[0]) and (card2[0] != card1[0] != card4[0] != card5[0]):
        sortedhand.remove(card2)
        sortedhand.remove(card3)
        return card2, card1, card4, card5
    elif (card3[0] == card4[0]) and (card3[0] != card1[0] != card2[0] != card5[0]):
        sortedhand.remove(card3)
        sortedhand.remove(card4)
        return card3, card1, card2, card5
    elif (card4[0] == card5[0]) and (card4[0] != card1[0] != card2[0] != card3[0]):
        sortedhand.remove(card4)
        sortedhand.remove(card5)
        return card4, card1, card2, card3
    else:
        return None

# returns a 3-tuple needed to compare
def is_two_pairs(sortedhand):
    card1 = sortedhand[0]
    card2 = sortedhand[1]
    card3 = sortedhand[2]
    card4 = sortedhand[3]
    card5 = sortedhand[4]
    if (card1[0] == card2[0]) and (card3[0] == card4[0]):
        # check it's not actually four of a kind or a full house
        if card1[0] != card3[0] and card1[0]!= card5[0] and card3[0]!=card5[0]:
            # card5 is the remaining card to check if both pairs are a tie
            return card1, card3, card5
        else:
            return None
    elif (card1[0] == card2[0]) and (card4[0]==card5[0]):
        # check it's not actually four of a kind or a full house
        if card1[0] != card4[0] and card1[0]!= card3[0] and card4[0]!=card3[0]:
            # card3 is the remaining card to check if both pairs are a tie
            return card1, card4, card3
        else:
            return None
    elif (card2[0] == card3[0]) and (card4[0]==card5[0]):
        # check it's not actually four of a kind or a full house
        if card2[0] != card4[0] and card2[0]!= card1[0] and card4[0]!=card1[0]:
            # card1 is the remaining card to check if both pairs are a tie
            return card2, card4, card1
        else:
            return None
    else:
        return None


def is_three_of_a_kind(sortedhand):
    card1 = sortedhand[0]
    card2 = sortedhand[1]
    card3 = sortedhand[2]
    card4 = sortedhand[3]
    card5 = sortedhand[4]
    if card1[0] == card2[0] == card3[0]:
        return card1, card4, card5
    elif card2[0] == card3[0] == card4[0]:
        return card2, card1, card5
    elif card3[0] == card4[0] == card5[0]:
        return card3, card1, card2
    else:
        # not three of a kind
        return None


def is_straight(sortedhand):
    card1 = sortedhand[0]
    card2 = sortedhand[1]
    card3 = sortedhand[2]
    card4 = sortedhand[3]
    card5 = sortedhand[4]
    if are_cards_consecutive(card1,card2):
        if are_cards_consecutive(card2,card3):
            if are_cards_consecutive(card3,card4):
                if are_cards_consecutive(card4,card5):
                    return card1, card5
    return None


def is_flush(sortedhand):
    card1 = sortedhand[0]
    card5 = sortedhand[4]
    suit1 = sortedhand[0][1]
    suit2 = sortedhand[1][1]
    suit3 = sortedhand[2][1]
    suit4 = sortedhand[3][1]
    suit5 = sortedhand[4][1]
    if suit1 == suit2 == suit3 == suit4 == suit5:
        return card1, card5
    else:
        return None


def is_full_house(sortedhand):
    card1 = sortedhand[0]
    card2 = sortedhand[1]
    card3 = sortedhand[2]
    card4 = sortedhand[3]
    card5 = sortedhand[4]
    if (card1[0] == card2[0] == card3[0]) and (card4[0] == card5[0]):
        return card1, card4
    elif (card1[0] == card2[0]) and (card3[0] == card4[0] == card5[0]):
        return card3, card1
    else:
        return None


def is_four_of_a_kind(sortedhand):
    card1 = sortedhand[0]
    card2 = sortedhand[1]
    card3 = sortedhand[2]
    card4 = sortedhand[3]
    card5 = sortedhand[4]
    if card1[0] == card2[0] == card3[0] == card4[0]:
        return card1, card5
    elif card2[0] == card3[0] == card4[0] == card5[0]:
        return card2, card1
    else:
        return None


def is_straight_flush(sortedhand):
    card1 = sortedhand[0]
    card5 = sortedhand[4]
    if not(is_flush(sortedhand) is None) and not(is_straight(sortedhand) is None):
        return card1, card5
    else:
        return None


def is_royal_flush(sortedhand):
    if not(is_flush(sortedhand) is None):
        card1 = sortedhand[0]
        card2 = sortedhand[1]
        card3 = sortedhand[2]
        card4 = sortedhand[3]
        card5 = sortedhand[4]
        if (card1[0] == 'T') and (card2[0] == 'J') and (card3[0] == 'Q') and (card4[0] == 'K') and (card5[0] == 'A'):
            return card1, card5
        else:
            return None
    else:
        return None

def hasGroupsSizeX(deck):
        deck_dict = {}
        for i in deck:
            if i not in deck_dict:
                deck_dict[i] = 1
            else:
                deck_dict[i] = deck_dict[i] + 1

        def gcd(remainder, dividend):
            if remainder == 0:
                return dividend
            return gcd(dividend % remainder, remainder)
        ans = 0
        for i in deck_dict:   
            ans = gcd(ans, deck_dict[i])
        if ans > 1:
            return True
        else:
            return False
              
        
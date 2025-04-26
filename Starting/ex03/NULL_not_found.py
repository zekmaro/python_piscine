# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anarama <anarama@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/04/26 14:39:44 by anarama           #+#    #+#              #
#    Updated: 2025/04/26 15:01:21 by anarama          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def NULL_not_found(obj: any) -> int:
    if obj is None:
        print(f"Nothing: {obj} {type(obj)}")
        return 0
    elif type(obj) == float and obj != obj:  # NaN: NaN != NaN is True
        print(f"Cheese: {obj} {type(obj)}")
        return 0
    elif type(obj) == int and obj == 0:
        print(f"Zero: {obj} {type(obj)}")
        return 0
    elif type(obj) == str and obj == '':
        print(f"Empty: {type(obj)}")
        return 0
    elif obj is False:
        print(f"Fake: {obj} {type(obj)}")
        return 0
    else:
        print("Type not Found")
        return 1


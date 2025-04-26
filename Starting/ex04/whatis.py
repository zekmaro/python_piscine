# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anarama <anarama@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/04/26 15:08:17 by anarama           #+#    #+#              #
#    Updated: 2025/04/26 15:09:12 by anarama          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
    if len(sys.argv) != 2:
        raise AssertionError("More than one argument is provided or no argument.")
    
    try:
        number = int(sys.argv[1])
    except ValueError:
        raise AssertionError("Argument is not an integer.")
    
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    main()

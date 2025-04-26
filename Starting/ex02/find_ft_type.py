# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anarama <anarama@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/04/26 14:26:31 by anarama           #+#    #+#              #
#    Updated: 2025/04/26 14:35:09 by anarama          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def all_thing_is_obj(object: any) -> int:
    type_name = type(object).__name__
    obj_type = type(object)
    if obj_type == str:
        print(f"{object.capitalize()} is in the kitchen: {obj_type}")
    else:
        print(f"{type_name.capitalize()}: {obj_type}")
    return 42

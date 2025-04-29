ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

new_list_tupple = list(ft_tuple)
new_list_tupple[1] = "Austria!"
ft_tuple = tuple(new_list_tupple)

ft_set.remove("tutu!")
ft_set.add("Vienna!")

ft_dict["Hello"] = "42Vienna!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
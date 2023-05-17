#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """ Replacing specific items """
    appd_list = my_list[:]
    list_len = len(my_list)

    for item in range(list_len):
		if appd_list[item] == search:
			appd_list[item] = replace

	return appd_list
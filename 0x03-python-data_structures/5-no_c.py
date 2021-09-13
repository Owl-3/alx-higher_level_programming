#!/usr/bin/python3
def no_c(my_string):
                alt_string = ""

                    i = 0

                        while (i < len(my_string)):
                                            if my_string[i] is not "c" and my_string[i] is not "C":
                                                                    alt_string += my_string[i]
                                                                            i = i + 1

                                                                                my_string = alt_string
                                                                                    return my_string
                                                                            # the new string is equal to itself plus my_string at i so we do
                                                                                # not reset the index of the string each loop.
                                                                                    # we need to return my_string, the original string
                                                                                    

#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
print(proto)
proto.extend('dns') # this line will add
                    # 'd', 'n', and 's' to
                    # the end of our list
print(proto)

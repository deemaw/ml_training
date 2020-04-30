
# url1 ='https://www.facebook.com/Cat-fish-102636517979742/?__tn__=kC-R&eid=ARA5wgpmbCDnN2Lc0zzzzbmq0ZfbkLvoC8dFO-3MFpXB3gUGVvZNQV8qqrbvZdK_EE7PMKnCSis9qLer&hc_ref=ARRpO11OeMJAh9Z5SNUlzhheF65P9BMofB8c0SIPbvoayMQ8mpfYslQIDbQFAFPQi2s&fref=nf&__xts__[0]=68.ARCg1mDXEY-xGbkXtpocC5EyblVeJkdh6kD2ynxFnyV9mqWtxbaP0vTPdnG1AuFeZAhM8P8Mv20U34s4ax7BZkaRL_UaVdzcSkKX21M4O_lGo1WAYVjLxzFxcitTzy4wIBXTXgkpYSuldjhg0JrqfkznvOzc0ftynPzFsjs_-jm87Rsm4ovswAMC-BFSKPoqvPy3MIKnoOb4Xv0LGh1DiKPEPb-ofjHAliXJoRLcVFwmChtplIlvXVMed6fbV0a0cEUXZOoC2rSz6ZOt0i72nPdcxKVRIjboZWVxHh91uUZ14kwDqTKBuKKI4GKWeYyf3pL175tQ9DRpZ65CoRg'
def get_postid(url):

    # Get the id of fb post
    startingindex = findSubstringIndex(url, "Cat-fish-") + len("Cat-fish-") 
    endingindex = findSubstringIndex(url, "/?__tn__=")
    return url[startingindex:endingindex]
        


def findSubstringIndex(string, substring):
    # Get the starting index of substring
    index = 0
    if substring in string: 
        c = substring[0]
        for ch in string:
            if ch == c:
                if string[index:index+len(substring)] == substring:
                    return index
            index += 1
    return -1

# pi = get_postid(url1)
# print(pi)
print(__name__)

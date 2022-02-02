def solution(progresses, speeds):
    count = 0
    result = []
    
    while len(progresses) != 0:
        progresses = [ x+y for x,y in zip(progresses,speeds)]
        if progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
              result.append(count)
              count = 0
    result.append(count)
    return result


# x라는 변수를 두고 반복되는 횟수를 곱해줘야 하는지?
#

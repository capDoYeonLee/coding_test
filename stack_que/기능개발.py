def solution(progresses, speeds):
    while len(speeds) != 0 :
      if speeds[i] + progresses[i] >= 100:
        speeds.pop(i)
        progresses.pop(i)
        count += 1
    
      else:
        s = [x + y for x,y in zip(s,p)]
    
    
def batting(p):
    points = p.get('runs')/2
   
    if p.get('runs') in range(50,100):
        points = points + 5
    elif p.get('runs')>=100:
         points = points + 10
   
    strike_rate=p.get('runs')/p.get('balls')*100
   
    if strike_rate in range(80,101):
            points = points + 2
    elif strike_rate > 100:
                points = points + 4
   
    points = points + p.get('4') + 2* p.get('6')+ p.get('field')*10
    
    return points


def bowling(p):
    points = p.get('wkts')*10
    if p.get('wkts') == 3:
        points = points + 5
    elif p.get('wkts') >= 5:
        points = points + 10
    erate = p.get('runs')/p.get('overs')
    
    if erate>3.5 and erate<4.6:
        points = points + 4
    elif erate>2 and erate<3.5:
        points = points + 7
    elif erate < 2:
        points = points + 10
    points = points + p.get('field')*10
    return points

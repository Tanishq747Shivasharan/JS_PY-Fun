# Variable Scope: Managing Configuration Levels

SECURITY_LEVEL = "High"

def keyword_previlage():
    global SECURITY_LEVEL 
    SECURITY_LEVEL = "Critical"
    print(SECURITY_LEVEL)

print(SECURITY_LEVEL)
keyword_previlage()
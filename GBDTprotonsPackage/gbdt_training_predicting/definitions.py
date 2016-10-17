
# The features that we want to use for the GBDT
feature_names = [
                 'nhits','length','starty','startz','endy','endz','theta','phi', 'distlenratio'    # geometry
                 ,'startdqdx','enddqdx','dqdxdiff','dqdxratio','totaldqdx','averagedqdx'            # calorimetry
                 ,'cosmicscore','coscontscore','pidpida','pidchi'                                    # uboonecode tagging and PID
                 ,'cfdistance'                                                                       # optical information - unused for open cosmic MC
                 ]

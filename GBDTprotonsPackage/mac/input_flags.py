import argparse

def get_args():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-v','--verbose', default='1', type=int , help='\n0 - quiet,\n1 - major functionality,\n2 - print out all sorts of shit')
    parser.add_argument('-p','--print_mod', default='1000', type=int , help='print every how many entries')
    parser.add_argument('-ff','--files_frac', default='0.01', type=float , help='fraction of files to process')
    parser.add_argument('-evf','--ev_frac', default='0.01', type=float , help='fraction of events to process')
    parser.add_argument('-w','--worker', default='erez', type=str )
    parser.add_argument('-mc','--MCmode', default='False', type=bool )
    
    
    debug = parser.parse_args().verbose
    print_every_entry = parser.parse_args().print_mod
    files_frac = parser.parse_args().files_frac
    ev_frac = parser.parse_args().ev_frac
    worker = parser.parse_args().worker
    MCmode = parser.parse_args().MCmode
    
    if debug>0: print "flags: ", parser.parse_args()
    
    return parser.parse_args()


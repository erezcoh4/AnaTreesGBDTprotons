# AnaTreesGBDTprotons

July-22,2016



dependencies:
-------------
larlite (http://github.com/larlight/larlite MyLArLite)




nessecities (for playing around at your local machine)
--------------
inside 

    PATH="/your_path_to_analysisTrees_examples/" 

you should have the following subdirectories:

    BDTanaFiles
    CSVOutFiles
    PassedGBDTFiles
    example_AnaTrees
    lists

and then download an example analysisTree file:

    /uboone/data/users/kwoodruf/proton_reco_mcc71/pandoraNu/ana_hist_bnb.root
    

and place it as:

    PATH/example_AnaTrees/ana_hist_bnb.root






example usage:
--------------
    > cd ~/larlite
    > source config/setup.sh
    > cd UserDev/AnaTreesGBDTprotons
    > make -j
    > python mac/calc_list_of_files.py --worker=erez --verbosity=1 -ff=1 -evf=0.01




flags:
--------------


    '-v'/'--verbose'
    default='1'
    type=int
    help='\n0 - quiet,\n1 - major functionality,\n2 - print out all sorts of shit'


    '-p','--print_mod'
    default='1000'
    type=int 
    help='print every how many entries'


    '-ff','--files_fraction'
    default='0.01'
    type=float
    help='fraction of files to process'


    '-evf','--ev_frac'
    default='0.01'
    type=float
    help='fraction of events to process from each analysis tree'


    '-w','--worker'
    default='erez'
    type=str




# Oct-14,2016
To start collecting data use

    python $macGBDTprotons/extract_anatrees_tracks_information_from_files_list.py -wuboone --DataType=extBNB --files_frac=0.001 --evnts_frac=0.1 -v4 -p1

(on the grid)
if this is MC data used for building the GBDTs, divide it to training and testing samples

    python $macGBDTprotons/divide_training_and_testing_samples.py -werez

now, we can train the GBDTs using Cross-Validation

    python gbdt_training_predicting/train_gbdt_cross_validation.py -werez -v1





















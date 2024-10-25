# test

      script/source.sh    --> Sets up PYTHONPATH and other environment variables

         ↓

      script/run_code.sh  --> Sets the JSON input file and launches app/plotter.py

         ↓

      app/plotter.py      --> Imports functions from python/plotter_libs.py
                           --> Reads parameters from json/29425.json
                           --> Loads data from paths defined in the JSON file
                           --> Performs processing and saves output to output_folder
